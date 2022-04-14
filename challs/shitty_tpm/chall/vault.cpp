#include <verilated.h>
#include <iostream>
#include <string>
#include "obj_dir/EasyTPM.h"

EasyTPM* tpm;


uint64_t main_time = 0;       

double sc_time_stamp() {        // Called by $time in Verilog
    return main_time;           // converts to double, to match
                                // what SystemC does
}


void resetTPM()
{
    tpm->rst = 1;
    for(int i = 0; i < 10; i++)
    {
        tpm->clk = 1;
        tpm->eval();
        tpm->clk = 0;
        tpm->eval();
    }
    tpm->rst = 0;
}

void sendChar(char c)
{
    tpm->data = c;
    tpm->clk = 1;
    tpm->eval();
    tpm->clk = 0;
    tpm->eval();

}


int main(int argc, char** argv) {


    std::cout << "Enter Password: " << std::endl;
    std::string line;
    std::getline(std::cin, line);
    if(line.length() < 8)
    {
        std::cout << "Input too short" << std::endl;
        return 0;
    }

    tpm = new EasyTPM;
    resetTPM();
    for(int i = 0; i < 8; i++)
    {
        sendChar(line[i]); // This sends one character to the TPM
    }

    if(tpm->lock == 1)
    {
        std::cout << "Good job, you got it!" << std::endl;
        std::cout << "DCTF{K3y_ch0s3n_by_f4ir_d1c3_roll}" << std::endl;
    }
    else
    {
        std::cout << "The vault is closed, try harder next time" << std::endl;
    }
}
