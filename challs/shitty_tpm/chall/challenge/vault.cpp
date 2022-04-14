#include <iostream>
#include <string>

int main(int argc, char** argv) {


    std::cout << "Enter Password: " << std::endl;
    std::string line;
    std::getline(std::cin, line);
    if(line.length() < 8)
    {
        std::cout << "Input too short" << std::endl;
        return 0;
    }
    // This is just pseudocode, for security
    // Kerckhoffs law is stupid anyway
    tpm = new EasyTPM;
    tpm->reset();
    for(int i = 0; i < 8; i++)
    {
        tpm->sendChar(line[i]); // This sends one character to the TPM
    }

    if(tpm->lock == 1)
    {
        std::cout << "Good job, you got it!" << std::endl;
        std::cout << "DUMMY_FLAG" << std::endl;
    }
    else
    {
        std::cout << "The vault is closed, try harder next time" << std::endl;
    }
}
