#ifndef DCTF_ASM_HPP
#define DCTF_ASM_HPP

#include <iostream>
#include <string>
#include <vector>
#include <stdexcept>
#include <iomanip>

namespace compiler
{
	struct Asm
	{
		virtual void build(std::vector<uint8_t> &bin) = 0;
		virtual int size() = 0;
		virtual void print() = 0;
	};
}

#endif
