#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <unistd.h>

void win() {
    FILE * flg;
    char buf[30];

    flg = fopen("flag.txt", "r");
    fscanf(flg, "%s", buf);
    printf("%s\n", buf);
}

void process_data(char * user_input);

int main () {
    char user_input[64];

    alarm(10);

    fgets(user_input, 0x64, stdin);
    process_data(user_input);
    return 0;
}

void process_data(char * user_input) {
    for(int i = 0; i < 64; i++) {
        char ch;
        ch = user_input[i] + (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11)*0 + 1;
        putchar(ch);
    }
    putchar('\n');
}
