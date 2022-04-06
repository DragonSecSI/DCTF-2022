#include "crypto.h"
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <errno.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <sodium.h>

int main() {

    // Read the flag
    FILE *file;
	char flag[33];
	file = fopen("flag.txt", "r");
	fgets(flag, 32, file);
	fclose(file);

    // Initialize the sodium crypto library.
    if(sodium_init() < 0) {
        printf("Error initializing sodium.\n");
        exit(EXIT_FAILURE);
    }

    // Create shared memory for communication
    int shared_memory_descriptor = shm_open(
        "/encryption_shared_memory",
        O_RDWR | O_CREAT,
        S_IRUSR | S_IWUSR
    );
    if(shared_memory_descriptor < 0) {
        printf("Error creating shared memory object: %d\n", errno);
        exit(EXIT_FAILURE);
    }

    // The initial size will be 0, set the size to 32 bytes instead
    if(ftruncate(shared_memory_descriptor, 32) < 0) {
        printf("Error setting shared memory object size: %d\n", errno);
        exit(EXIT_FAILURE);
    }

    // Map the shared memory into this address space
    char* shared_memory = mmap(
        NULL,
        32,
        PROT_READ | PROT_WRITE,
        MAP_SHARED,
        shared_memory_descriptor,
        0
    );
    if(shared_memory == NULL) {
        printf("Error mapping shared memory: %d\n", errno);
        exit(EXIT_FAILURE);
    }

    int i = 0;
    // Wait to receive a message
    while(1) {

        // Wait untill we get a message
        while(1) {
            char got_message = *shared_memory;
            if(got_message) {
                break;
            }
        }

        char message[16];
        strcpy(message, shared_memory+1);

        // Get the i-th nibble of the flag
        //printf("Character is %c, ascii is %x\n", flag[i/2], flag[i/2]);
        int nibble = (flag[i / 2] & 0xff) >> (((i+1) % 2) * 4) & 0xf;
        //printf("Nibble is %x\n", nibble);

        // Encrypt the message
        char ciphertext[crypto_secretbox_MACBYTES + 16];
        my_encrypt(nibble, flag, message, ciphertext);

        i = (i + 1) % 64;

        for(int i = 1; i < 17; i++) {
            shared_memory[i] = ciphertext[crypto_secretbox_MACBYTES + i - 1];
        }
        *shared_memory = 0;
    }

    return 0;
}