#include "crypto.h"

void my_encrypt(int i, char* key, char* pt, char* ct) {
    // Get an XOR mask
    char xor_mask[16];
    switch(i) {
        case 0: mask_0(xor_mask); break;
        case 1: mask_1(xor_mask); break;
        case 2: mask_2(xor_mask); break;
        case 3: mask_3(xor_mask); break;
        case 4: mask_4(xor_mask); break;
        case 5: mask_5(xor_mask); break;
        case 6: mask_6(xor_mask); break;
        case 7: mask_7(xor_mask); break;
        case 8: mask_8(xor_mask); break;
        case 9: mask_9(xor_mask); break;
        case 10: mask_10(xor_mask); break;
        case 11: mask_11(xor_mask); break;
        case 12: mask_12(xor_mask); break;
        case 13: mask_13(xor_mask); break;
        case 14: mask_14(xor_mask); break;
        case 15: mask_15(xor_mask); break;
        default: mask_0(xor_mask);
    }

    // xor the plaintext with the mask
    for(int i = 0; i < 16; i++) {
        pt[i] ^= pt[i];
    }

    // Encrypt the plaintext using the key
    unsigned char nonce[crypto_secretbox_NONCEBYTES];
    randombytes_buf(nonce, sizeof nonce);
    int status = crypto_secretbox_easy(
        (unsigned char*)ct,
        (unsigned char*)pt,
        16,
        nonce,
        (unsigned char*)key
    );
    if(status < 0) {
        printf("Encryption error\n");
        exit(EXIT_FAILURE);
    }
}

void mask_0(char* mask) { memcpy(mask, "0000000000000000", 16); }
void mask_1(char* mask) { memcpy(mask, "1111111111111111", 16); }
void mask_2(char* mask) { memcpy(mask, "2222222222222222", 16); }
void mask_3(char* mask) { memcpy(mask, "3333333333333333", 16); }
void mask_4(char* mask) { memcpy(mask, "4444444444444444", 16); }
void mask_5(char* mask) { memcpy(mask, "5555555555555555", 16); }
void mask_6(char* mask) { memcpy(mask, "6666666666666666", 16); }
void mask_7(char* mask) { memcpy(mask, "7777777777777777", 16); }
void mask_8(char* mask) { memcpy(mask, "8888888888888888", 16); }
void mask_9(char* mask) { memcpy(mask, "9999999999999999", 16); }
void mask_10(char* mask) { memcpy(mask, "aaaaaaaaaaaaaaaa", 16); }
void mask_11(char* mask) { memcpy(mask, "bbbbbbbbbbbbbbbb", 16); }
void mask_12(char* mask) { memcpy(mask, "cccccccccccccccc", 16); }
void mask_13(char* mask) { memcpy(mask, "dddddddddddddddd", 16); }
void mask_14(char* mask) { memcpy(mask, "eeeeeeeeeeeeeeee", 16); }
void mask_15(char* mask) { memcpy(mask, "ffffffffffffffff", 16); }