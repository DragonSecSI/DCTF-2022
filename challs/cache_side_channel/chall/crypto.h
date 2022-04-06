#include <stdlib.h>
#include <string.h>
#include <sodium.h>

typedef struct {
    long type;
    char payload[17];
} queuedMessage;

void my_encrypt(int i, char* key, char* pt, char* ct);

void mask_0(char* mask);
void mask_1(char* mask);
void mask_2(char* mask);
void mask_3(char* mask);
void mask_4(char* mask);
void mask_5(char* mask);
void mask_6(char* mask);
void mask_7(char* mask);
void mask_8(char* mask);
void mask_9(char* mask);
void mask_10(char* mask);
void mask_11(char* mask);
void mask_12(char* mask);
void mask_13(char* mask);
void mask_14(char* mask);
void mask_15(char* mask);