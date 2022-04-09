#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int generate_padawan(int i, int padawans[], int curr) {
    if (curr <= 2) {
        padawans[curr] = 1;
    } else {
        padawans[curr] = padawans[curr-2] + padawans[curr-3];
    }
    if (curr == i) {
        return padawans[curr];
    } else {
        return generate_padawan(i, padawans, curr+1);
    }
}

int main() {
    time_t t;   
    srand((unsigned) time(&t));
    int i = 40 + (rand() % 10);
    int* padawans = malloc(50 * sizeof(int));
    int p = generate_padawan(i, padawans, 0);
    printf("%d\n", i);
    int u = 0;
    time_t start = time(NULL);
    scanf("%d", &u);
    time_t end = time(NULL);
    if (end - start > 1) {
        printf("Too slow, young Padawan.\n");
        exit(1);
    }
    
    if (u == p) {
        printf("dctf{pr0uD_0F_y0u_yOuNg_Padovan}\n");
    } else {
        printf("Much to learn, you still have.\n");
    }
}