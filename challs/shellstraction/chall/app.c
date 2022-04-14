#include <stdio.h>
#include <signal.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <string.h>
#include <ctype.h>
#include <errno.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <dirent.h>
#include <fcntl.h>
#include <sys/file.h>

// AG
char* user;
char* host;
char path[200];

int guard = 0;
char* notes;

// RE
int token_count;
char* tokens[50];           // token pointers array limited to 50 pointers??
char* sh_name;
int statp;
int background = 0;
int file_in = 0;
char* file_in_name;
int file_out = 0;
char* file_out_name;
int lastex = 0;

// sighandler
void process(int s) {
    switch (s) {
        case 17: // SIGCHLD
            wait(&statp);
            return;
    }
}

// stores pointers to the first characters of tokens/multitokens (tokens wrapped in quotation marks) in the global tokens array
// this function does not check for tokens array bounderies
void tokenize(char* line) {
    token_count = 0;
    int newtoken = 1;
    int multitoken = 0;
    if (line[0] == '#') {
        return;
    }
    int len = strlen(line);
    for (int i = 0; i < len; i++) {
        char curr = line[i];
        //printf(":%c: %d %d %d\n", curr, token_count, newtoken, multitoken);
        if (newtoken == 1) {
            // check for max token count
            if (token_count > 50) {
                puts("Too many tokens.");
                return;
            }

            if (isspace(curr) != 0) {        // isspace checks for white-space character, returns nonzero if curr is a white-space
                line[i] = '\0';
                continue;
            }
            if (curr == '"') {
                multitoken = 1;
                tokens[token_count] = &(line[i+1]);
            }
            else {
                multitoken = 0;
                tokens[token_count] = &(line[i]);       // it stores address of the first char of the token in the tokens array
            }
            newtoken = 0;

            token_count++;
            continue;
        }
        if ((multitoken == 1 && curr == '"') || (multitoken == 0 && isspace(curr))) {
            line[i] = '\0';
            newtoken = 1;
        }
    }
}

void name() {
    if (token_count == 1) {
        printf("%s\n", sh_name);
        fflush(stdout);
    } else {
        strncpy(sh_name, tokens[1], 100);
    }
    lastex = 0;
}

// my favourite function, thanks Mitič, very cool
void help() {
    printf("Help me!\n");
    fflush(stdout);
    lastex = 0;
}

void whoami() {
    printf("%s\n", user);
    fflush(stdout);
    lastex = 0;
}

void hostname() {
    printf("%s\n", host);
    fflush(stdout);
    lastex = 0;
}

void eton() {
    if (!guard) {
        puts("Not enough memory available.");
        lastex = -1;
        return;
    }

    if (token_count < 2) {
        puts("Not enough arguments for command note");
        lastex = 0;
        return;
    }

    if (strcmp(tokens[1], "help") == 0) {
        puts("This is a simple shell program for saving personal notes!");
    } else if (strcmp(tokens[1], "add") == 0) {
        if (token_count < 3) {
            puts("Not enough arguments for command note");
            lastex = 0;
            return;
        }
        puts("Creating a note...");
        sleep(1);
        notes = (char*) malloc(50);
        if (notes != NULL) {
            strcpy(notes, tokens[2]);
        }
        puts("Note created");
    } else if (strcmp(tokens[1], "remove") == 0) {
        puts("Removing notes...");
        sleep(1);
        free(notes);
        puts("Notes removed.");
    } else if (strcmp(tokens[1], "show") == 0) {
        printf("%s\n", notes);
    } else {
        puts("Invalid argument for command note");
    }

    lastex = 0;
}

void exit_shell() {
    if (token_count == 1) {
        exit(0);
    } else {
        exit(atoi(tokens[1]));
    }
}

void status() {
    printf("%d\n", lastex);
    fflush(stdout);
    lastex = 0;
}

void print() {
    if (token_count > 1) printf("%s", tokens[1]);
    for (int i = 2; i < token_count; i++) {
        printf(" %s", tokens[i]);
    }
    fflush(stdout);
    lastex = 0;
}

void echo() {
    print();
    printf("\n");
    fflush(stdout);
    lastex = 0;
}

// cd
void dirchange() {
    int out = 0;
    if (token_count == 1) {
        out = chdir("/");
    } else {
        out = chdir(tokens[1]);   
    }
    if (out != 0) {
        lastex = errno;
        perror("cd");
        fflush(stdout);
    } else if (getcwd(path, sizeof(path)) == NULL) {
        perror("dirchange");
        fflush(stdout);
        lastex = errno;
    } else {
        lastex = out;
    }
}

// pwd
void dirwhere() {
    if (getcwd(path, sizeof(path)) != NULL) {
        printf("%s\n", path);
        fflush(stdout);
        lastex = 0;
    } else {
        lastex = errno;
        perror("pwd");
        fflush(stdout);
    }
}

// mkdir
void dirmake() {
    int out = mkdir(tokens[1], 0755);
    if (out != 0) {
        lastex = errno;
        perror("mkdir");
        fflush(stdout);
    }
    else lastex = 0;
}

// ls
// prints dir entries, not sorted
void dirlist() {
    struct dirent *entry;
    DIR *dir;
    if (token_count == 1) {
        char cwd[200];
        if (getcwd(cwd, sizeof(cwd)) == NULL) {
            lastex = errno;
            perror("ls");
            fflush(stdout);
            return;
        }
        dir = opendir(cwd);
    }
    else {
        dir = opendir(tokens[1]);
    }

    if (dir == NULL) {
        lastex = errno;
        perror("ls");
        fflush(stdout);
        return;
    }

    char* dirs[100];
    int counter = 0;
    while ((entry = readdir(dir)) != NULL) {
        char* nm = (entry->d_name);
        //printf("%s ", nm);
        //if (strcmp(".", nm) == 0 || strcmp("..", nm) == 0) continue;
        dirs[counter++] = nm;
    }
    if (counter > 0) printf("%s", dirs[0]);
    for (int i = 1; i < counter; i++) {
        printf("  %s", dirs[i]);
    }
    printf("\n");
    lastex = 0;
}

// creates a file with a given path and only with read perms for everybody
void touch() {
    int i = 0;
    signed char offset = 0;

    if (token_count < 2) {
        puts("Too few arguments for command touch.");
        return;
    }

    memset(dirs, 0, 100);

    for (i = 1; i < token_count; i++) {
        // copy dir's name from tokens array onto the stack
        // there is 50 tokens max
        offset += strlen(tokens[i]);

        // create a dir with a given name
        int f = creat(tokens[i], 00444);
        if (f == -1) {
            perror("touch");
            fflush(stdout);
            lastex = errno;
            return;
        } else lastex = 0;
    }

    if (offset < 0) {
        guard = 1;
    }

    printf("%s\n", dirs);
}

int main(int argc, char **argv) {
	signal(SIGCHLD, process);

    sh_name = (char*) malloc(100);
    user = (char*) malloc(20);
    host = (char*) malloc(20);

	strcpy(sh_name, "agresh - The AlwaysGuilty-Red_Epicness Shell");
    strcpy(user, "competitor");
    strcpy(host, "shellstraction");

    if (getcwd(path, sizeof(path)) == NULL) {
        perror("getcwd");
        lastex = errno;
        exit(lastex);
    }

	while (1) {
	    char* line = NULL;
	    size_t size = 0;
	    if (isatty(1)) {
            printf("%s@%s:%s$ ", user, host, path);
        }
	    int out = getline(&line, &size, stdin);         // stores pointer to buffer to *lineptr and updates *n with buffer size, returns number of chars read
	    if (out == -1) {                                // failure or EOF
	        return 0;
	    }
	    tokenize(line);
	    if (token_count == 0) {
	        continue;
	    }


        // should we run this program in the background?
	    if (strcmp(tokens[token_count - 1], "&") == 0) {
	        background = 1;
	        token_count--;
	    } else {
	        background = 0;
	    }

        // order of file redirection: <inFile, >outFile, &

        // redirect output into another file?
	    if (tokens[token_count - 1][0] == '>') {
	        file_out = 1;
	        file_out_name = &(tokens[token_count-1][1]);
	        token_count--;
	    } else {
	        file_out = 0;
	    }

        // redirect input from another file?
	    if (tokens[token_count - 1][0] == '<') {
	        file_in = 1;
	        file_in_name = &(tokens[token_count-1][1]);
	        token_count--;
	    } else {
	        file_in = 0;
	    }

	    /* printf("\nTokens:\n");
	    for (int i = 0; i < token_count; i++) {
	        printf(":%s:\n", tokens[i]);
	    }
	    printf("Modifiers: IN_REDIR=%d (%s) OUT_REDIR=%d (%s) BKGRND=%d\n\n", file_in, file_in_name, file_out, file_out_name, background); */

        // creating background process
	    int cpid1 = -1;
	    if (background == 1) {
	        cpid1 = fork();
	        if (cpid1 != 0) continue;       // if not in child, continue
	    }

        // open files for redirecting input/output
	    FILE* old_stdout = stdout;
	    if (file_out == 1) {
	        stdout = fopen(file_out_name, "w");
            if (stdout == NULL) {
                stdout = old_stdout;
                perror("Output redirection");
                fflush(stdout);
                continue;               // are errors here handled correctly? i don't know.
            }
	    }

	    FILE* old_stdin = stdin;
	    if (file_in == 1) {
	        stdin = fopen(file_in_name, "r");
            if (stdin == NULL) {
                stdin = old_stdin;
                perror("Input redirection");
                fflush(stdout);
                continue;
            }
	    }

        // evaluating the tokens
	    if (strcmp(tokens[0], "name") == 0)             name();
	    else if (strcmp(tokens[0], "help") == 0)        help();
        else if (strcmp(tokens[0], "whoami") == 0)      whoami();
        else if (strcmp(tokens[0], "hostname") == 0)    hostname();
	    else if (strcmp(tokens[0], "status") == 0)      status();
	    else if (strcmp(tokens[0], "exit") == 0)        exit_shell();
	    else if (strcmp(tokens[0], "print") == 0)       print();
	    else if (strcmp(tokens[0], "echo") == 0)        echo();
	    else if (strcmp(tokens[0], "cd") == 0)          dirchange();
	    else if (strcmp(tokens[0], "pwd") == 0)         dirwhere();
	    else if (strcmp(tokens[0], "mkdir") == 0)       dirmake();
	    else if (strcmp(tokens[0], "ls") == 0)          dirlist();
        else if (strcmp(tokens[0], "touch") == 0)       touch();
        else if (strcmp(tokens[0], "note") == 0)        eton();
	    else puts("Unknown command.");
        
        // are we in the child process?
	    if (cpid1 == 0) {
	        exit(lastex);
	        return lastex;
	    }
        // handlers for inpt/output redirection finalization
	    if (file_out == 1) {
	        stdout = old_stdout;
	    }
	    if (file_in == 1) {
	        stdin = old_stdin;
	    }
	}

    free(sh_name);
    free(user);
    free(host);

    return 0;
}
