#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <unistd.h>

void hehe(int a, int b) {
    FILE * flg;
    char buf[30];
    
    if(a == 1337)
        flg = fopen("flag.txt", "r");

    if(b == 0x420)
        fscanf(flg, "%s", buf);

    printf("%s\n", buf);
}

void process_data(char * user_input);

int main () {
    char user_input[48];
    alarm(10);

    printf("uh oh a bit harder one:)\n");
    fgets(user_input, 0x64, stdin);
    process_data(user_input);
    return 0;
}

void process_data(char * user_input) {
    for(int i = 1; i < 46; i++){
        int x = user_input[i];
        int j = i - 1;
        for(; j >= 0 && user_input[j] > x; j--) {
            user_input[j + 1] = user_input[j];
        }
        user_input[j+1] = x;
    }
    printf("%s\n", user_input);
    printf("done!\n");
}
