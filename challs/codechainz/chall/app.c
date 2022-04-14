#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/mman.h>
#include <stdbool.h>
#include <errno.h>

char* memory_space;

/** 30 B http://shell-storm.org/input/files/input-603.php
    char* input =
    "\x48\x31\xd2"
    "\x48\xbb\x2f\x2f\x62\x69\x6e\x2f\x73\x68"
    "\x48\xc1\xeb\x08"                         
    "\x53"
    "\x48\x89\xe7"
    "\x50"
    "\x57"
    "\x48\x89\xe6"
    "\xb0\x3b"
    "\x0f\x05";
*/

void init_memory() {
    memory_space = mmap(NULL, 30, PROT_READ | PROT_EXEC | PROT_WRITE, 0x22, -1, 0);
    if (memory_space == MAP_FAILED) {
        perror("mmap");
        fflush(stdout);
        exit(errno);
    }
}

void welcome() {
    puts("Hey, this is an epic memory saver. #saved");
    puts("Because of COVID-19 restrictions,");
    puts("we can only do memory saving of programming languages.");
    puts("We apologize for the inconvenience.\n");

    puts("Preparing the memory space...");
    sleep(1);
    init_memory();
    puts("Memory space is ready for storing data.");
    printf("DISCLAIMER: All your memories will be saved at %p.\n\n\n", memory_space);
}

void menu() {
    puts("Here are your options. Choose one:");
    puts("1  Make a new memory");
    puts("2  View a memory");
    puts("3  Delete a memory");
    puts("4  Exit");
}

void input_int(int* a) {
    printf("> ");
    fflush(stdout);
    int result = scanf("%d", a);
    fflush(stdin);
    if (result < 0) {
        printf("scanf error, exiting...");
        exit(1);
    } 
    //fflush(stdout);
}

void input_str() {
    char buffer[30];
    memset(buffer, 0, 30);
    puts("Please input a programming language of your desire. I swear i will remember it.");
    printf("> ");
    fflush(stdout);
    fgets(buffer, 100, stdin);          // this will read 99 chars to buffer, including one newline char. It will also append a nullbyte
    for (int i = 0; i < 30; i++) {
        memory_space[i] = buffer[i];
        //printf("%c - %c\n", buffer[i], memory_space[i]);        // debug
    }
    fflush(stdin);
}

void loop_de_loop() {
    int choice = -1;
    bool is_memory_made = false;

    while (1) {
        menu();
        fflush(stdout);
        input_int(&choice);
        switch (choice) {
            case 1:     // reads a string, copies it from stack to mmaped memory
                if (!is_memory_made) {
                    char stupid[10];
                    fgets(stupid, 2, stdin);
                    input_str();
                    is_memory_made = true;
                } else {
                    puts("You have already made a memory!\n");
                }
                break;
            case 2:
                if (is_memory_made) {
                    puts("Here is your memory. I managed to remember it ^^");
                    printf("%s\n", memory_space);
                } else {
                    puts("You have no memories saved.\n");
                }
                break;
            case 3:
                if (is_memory_made) {
                    puts("Deleting your memory...");
                    memset(memory_space, 0, 30);
                    is_memory_made = false;
                    sleep(2);
                    puts("Memory deleted.\n");
                } else {
                    puts("You have no memories saved.\n");
                }
                break;
            case 4:
                puts("Goodbye!");
                exit(0);
            default:
                puts("Invalid option.\n");
                break;
        }
    }
}

int main() {
    alarm(20);
    welcome();
    loop_de_loop();
    return 0;
}