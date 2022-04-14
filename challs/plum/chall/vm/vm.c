#include <stdio.h>
#include <stdlib.h>
#include <openssl/sha.h>
#include <string.h>

//#define DEBUG

const int regs_size = 32;
int regs[regs_size] = {0};

void xor(){
    char *buf;
    long f_size;
    unsigned char key[SHA512_DIGEST_LENGTH];
    char fname[128];

    FILE *f = fopen("bin", "r");
    fseek(f, 0, SEEK_END);
    f_size = ftell(f);
    fseek(f, 0, SEEK_SET);
    buf = malloc(f_size+1);
    fread(buf, f_size, 1, f);
    fclose(f);

    SHA512_CTX ctx;
    SHA512_Init(&ctx);
    SHA512_Update(&ctx, buf, f_size);
    SHA512_Final(key, &ctx);

    free(buf);

    printf("Enter path to the file you want to encrypt: ");
    scanf("%s", fname);
    FILE *pt = fopen(fname, "r");
    fseek(pt, 0, SEEK_END);
    f_size = ftell(pt);
    fseek(pt, 0, SEEK_SET);
    buf = malloc(f_size+1);
    fread(buf, f_size, 1, pt);
    fclose(pt);

    for(int i = 0; i < f_size; i++){
        buf[i] ^= key[i%SHA512_DIGEST_LENGTH];
    }

    printf("Enter path to where you want to save the result: ");
    scanf("%s", fname);
    FILE *ct = fopen(fname, "w");
    fwrite(buf, f_size, 1, ct);
}

#ifdef DEBUG
void debug(){
    char str[128] = "";
    for (int i = 0; i < regs_size; i++)
    {
        char tmp[4];
        sprintf(tmp, "%d,", regs[i]);
        strcat(str, tmp);
    }

		puts(str);
}
#endif

void reghash(){
    char str[128] = "";
    unsigned char hash[SHA256_DIGEST_LENGTH];

    for (int i = 0; i < regs_size; i++)
    {
        char tmp[4];
        sprintf(tmp, "%d,", regs[i]);
        strcat(str, tmp);
    }
    SHA256_CTX ctx;
    SHA256_Init(&ctx);
    SHA256_Update(&ctx, str, strlen(str));
    SHA256_Final(hash, &ctx);
    for(int i = 0; i < SHA256_DIGEST_LENGTH; i++){
        printf("%02x", hash[i]);
    }
    printf("\n");
}

int main(){
    char** strings = malloc(2048);
    int sidx = 0;
    char ins, c, n;
    FILE *f = fopen("bin", "r");
    
    while ((ins = fgetc(f)) != EOF) {
				#ifdef DEBUG
				debug();
				#endif
        switch (ins) {
            // read global strings
            case 0:
                strings[sidx] = calloc(512, 1);
                for(int i = 0; c = fgetc(f); i++){
                    strings[sidx][i] = c;
                }
                sidx++;
                break;
            // skip n bytes
            case 1:
                n = fgetc(f);
                for(int i = 0; i < n; i++) fgetc(f);
                break;
            // je n reg
            case 2:
                n = fgetc(f);
                if (regs[fgetc(f)] == 0) {
                    for(int i = 0; i < n; i++) fgetc(f);
                }
                break;
            // read int to reg
            case 3:
                scanf("%d", &regs[fgetc(f)]);
                break;
            // print string n
            case 4:
                printf("%s\n", strings[fgetc(f)]);
                break;
            // encrypt/decrypt
            case 5:
                xor();
                break;
            // reghash
            case 6:
                reghash();
                break;
            // exit
            case 7:
                exit(0);
                break;
            // load reg val
            case 8:
            {
                char reg = fgetc(f);
                char val = fgetc(f);
                regs[reg] = val;
                break;
            }
            
            //bin ops ... r1 <= r2 x r3
            // add
            case 11:
            {
                char reg_dest = fgetc(f);
                char reg_1 = fgetc(f);
                char reg_2 = fgetc(f);
                regs[reg_dest] = regs[reg_1] + regs[reg_2];
                break;
            }
            // sub
            case 12:
            {
                char reg_dest = fgetc(f);
                char reg_1 = fgetc(f);
                char reg_2 = fgetc(f);
                regs[reg_dest] = regs[reg_1] - regs[reg_2];
                break;
            }
            // mul
            case 13:
            {
                char reg_dest = fgetc(f);
                char reg_1 = fgetc(f);
                char reg_2 = fgetc(f);
                regs[reg_dest] = regs[reg_1] * regs[reg_2];
                break;
            }
            // div
            case 14:
            {
                char reg_dest = fgetc(f);
                char reg_1 = fgetc(f);
                char reg_2 = fgetc(f);
                regs[reg_dest] = regs[reg_1] / regs[reg_2];
                break;
            }
            // mod
            case 15:
            {
                char reg_dest = fgetc(f);
                char reg_1 = fgetc(f);
                char reg_2 = fgetc(f);
                regs[reg_dest] = regs[reg_1] % regs[reg_2];
                break;
            }
            // geq
            case 16:
            {
                char reg_dest = fgetc(f);
                char reg_1 = fgetc(f);
                char reg_2 = fgetc(f);
                regs[reg_dest] = regs[reg_1] >= regs[reg_2];
                break;
            }
            // leq
            case 17:
            {
                char reg_dest = fgetc(f);
                char reg_1 = fgetc(f);
                char reg_2 = fgetc(f);
                regs[reg_dest] = regs[reg_1] <= regs[reg_2];
                break;
            }
            // eq
            case 18:
            {
                char reg_dest = fgetc(f);
                char reg_1 = fgetc(f);
                char reg_2 = fgetc(f);
                regs[reg_dest] = regs[reg_1] == regs[reg_2];
                break;
            }
						default:
							putc(ins, stderr);
        }
    }
}
