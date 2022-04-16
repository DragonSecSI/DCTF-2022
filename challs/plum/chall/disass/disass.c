#include <stdio.h>
#include <stdlib.h>
#include <openssl/sha.h>
#include <string.h>


int main(int argc, char* argv[])
{
		if (argc <= 1)
		{
			printf("Usage: %s <file>\n", argv[0]);
			return 1;
		}

    int sidx = 0;
    char ins, c, n;
    FILE *f = fopen(argv[1], "r");
    
    while ((ins = fgetc(f)) != EOF) {
        switch (ins) {
            // read global strings
            case 0:
								printf("[String] n:%d: ", sidx);
                for(int i = 0; c = fgetc(f); i++){
										printf("%c", c);
                }
								printf("\n");
                sidx++;
                break;
            // skip n bytes
            case 1:
								printf("[Skip] n:%d\n", fgetc(f));
                break;
            // je n reg
            case 2:
                n = fgetc(f);
								printf("[JE] n:%d reg:%d\n", n, fgetc(f));
                break;
            // read int to reg
            case 3:
								printf("[Read] reg:%d\n", fgetc(f));
                break;
            // print string n
            case 4:
                printf("[Print] n:%d\n", fgetc(f));
                break;
            // encrypt/decrypt
            case 5:
								printf("[Mangle]\n");
                break;
            // reghash
            case 6:
								printf("[Reghash]\n");
                break;
            // exit
            case 7:
								printf("[Exit]\n");
                break;
            // load reg val
            case 8:
            {
                char reg = fgetc(f);
                char val = fgetc(f);
								printf("[Load] reg:%d val:%d\n", reg, val);
                break;
            }
            
            //bin ops ... r1 <= r2 x r3
            // add
            case 11:
            {
                char reg_dest = fgetc(f);
                char reg_1 = fgetc(f);
                char reg_2 = fgetc(f);
								printf("[BinOp +] dst:%d 1:%d 2:%d\n", reg_dest, reg_1, reg_2);
                break;
            }
            // sub
            case 12:
            {
                char reg_dest = fgetc(f);
                char reg_1 = fgetc(f);
                char reg_2 = fgetc(f);
								printf("[BinOp -] dst:%d 1:%d 2:%d\n", reg_dest, reg_1, reg_2);
                break;
            }
            // mul
            case 13:
            {
                char reg_dest = fgetc(f);
                char reg_1 = fgetc(f);
                char reg_2 = fgetc(f);
								printf("[BinOp *] dst:%d 1:%d 2:%d\n", reg_dest, reg_1, reg_2);
                break;
            }
            // div
            case 14:
            {
                char reg_dest = fgetc(f);
                char reg_1 = fgetc(f);
                char reg_2 = fgetc(f);
								printf("[BinOp /] dst:%d 1:%d 2:%d\n", reg_dest, reg_1, reg_2);
                break;
            }
            // mod
            case 15:
            {
                char reg_dest = fgetc(f);
                char reg_1 = fgetc(f);
                char reg_2 = fgetc(f);
								printf("[BinOp %] dst:%d 1:%d 2:%d\n", reg_dest, reg_1, reg_2);
                break;
            }
            // geq
            case 16:
            {
                char reg_dest = fgetc(f);
                char reg_1 = fgetc(f);
                char reg_2 = fgetc(f);
								printf("[BinOp >=] dst:%d 1:%d 2:%d\n", reg_dest, reg_1, reg_2);
                break;
            }
            // leq
            case 17:
            {
                char reg_dest = fgetc(f);
                char reg_1 = fgetc(f);
                char reg_2 = fgetc(f);
								printf("[BinOp <=] dst:%d 1:%d 2:%d\n", reg_dest, reg_1, reg_2);
                break;
            }
            // eq
            case 18:
            {
                char reg_dest = fgetc(f);
                char reg_1 = fgetc(f);
                char reg_2 = fgetc(f);
								printf("[BinOp ==] dst:%d 1:%d 2:%d\n", reg_dest, reg_1, reg_2);
                break;
            }
						default:
								printf("[Garbage] %c\n", ins);
        }
    }
}
