#include <stdio.h>
#include <stdint.h>

uint32_t fun_array[] = {51339, 50768, 59432, 52322, 63068, 34398, 53481, 24718, 40495, 58937, 26176, 48660, 28311, 53371, 26273, 48805, 58430, 25178, 52974, 53421, 28301, 48869, 55955, 24671, 55964, 26366, 56422, 59637, 48794, 28840, 26873, 60667, 56374, 50256, 24582, 64013};

uint32_t bytes[] = {0x8b, 0x50, 0x28, 0x62, 0x5c, 0x5e, 0xe9, 0x8e, 0x2f, 0x39, 0x40, 0x14, 0x97, 0x7b, 0xa1, 0xa5, 0x3e, 0x5a, 0xee, 0xad, 0x8d, 0xe5, 0x93, 0x5f, 0x9c, 0xfe, 0x66, 0xf5, 0x9a, 0xa8, 0xf9, 0xfb, 0x36, 0x50, 0x6, 0xd};

void get_input(int* a) {
    scanf("%d", a);
    if (*a > 10 || *a < 0) {
        puts("Invalid input! Try again!");
        get_input(a);
    } else {
        puts("Thanks for your opinion!");
        return;
    }
}

void prompt(int* a) {
    puts("How would you rate Star Wars? [0-10]");
    get_input(a);
    return;
}

void encode(int* a) {
    for (int i = 0; i < 36; i++) {
        fun_array[i] = (uint32_t)fun_array[i] + *a;       // plus num
        fun_array[i] <<= 0x9;                        // shift left
        fun_array[i] -= (*a << 0x9);                 // sub left shifted num 
        fun_array[i] ^= bytes[i];                    // xor
        //printf("%u ", fun_array[i]);
    }
    puts("");
    return;
}

void decode(int* a) {
    for (int i = 0; i < 36; i++) {
        fun_array[i] ^= bytes[i];
        fun_array[i] += (*a << 0x9);
        fun_array[i] >>= 0x9;
        fun_array[i] -= *a;
    }
    return;
}

/* void print_flag() {
    for (int i = 0; i < 36; i++) {
        printf("%d ", fun_array[i]);
    }
    puts("");
} */

int main() {
    int num;
    prompt(&num);
    decode(&num);
    //print_flag();
    encode(&num);
    return 0;
} 