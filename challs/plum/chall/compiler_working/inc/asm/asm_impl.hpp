#ifndef DCTF_ASM_IMPL_HPP
#define DCTF_ASM_IMPL_HPP

#include <string>
#include <vector>

#include "asm/asm.hpp"
#include "nodes/nodes.hpp"

namespace compiler
{
	struct AsmString : Asm
	{
		std::vector<uint8_t> string;

		void build(std::vector<uint8_t> &bin);
		int size();
		void print();
	};

	struct AsmSkip : Asm
	{
		uint8_t n;

		void build(std::vector<uint8_t> &bin);
		int size();
		void print();
	};

	struct AsmJE : Asm
	{
		uint8_t reg;
		uint8_t n;

		void build(std::vector<uint8_t> &bin);
		int size();
		void print();
	};

	struct AsmRead : Asm
	{
		uint8_t reg;

		void build(std::vector<uint8_t> &bin);
		int size();
		void print();
	};

	struct AsmPrint : Asm
	{
		uint8_t i;

		void build(std::vector<uint8_t> &bin);
		int size();
		void print();
	};

	struct AsmMangle : Asm
	{
		void build(std::vector<uint8_t> &bin);
		int size();
		void print();
	};

	struct AsmReghash : Asm
	{
		void build(std::vector<uint8_t> &bin);
		int size();
		void print();
	};

	struct AsmExit : Asm
	{
		void build(std::vector<uint8_t> &bin);
		int size();
		void print();
	};

	struct AsmLoad : Asm
	{
		uint8_t reg;
		uint8_t val;

		void build(std::vector<uint8_t> &bin);
		int size();
		void print();
	};

	struct AsmBinOpAdd : Asm
	{
		uint8_t reg_dest;
		uint8_t reg_1;
		uint8_t reg_2;
		
		void build(std::vector<uint8_t> &bin);
		int size();
		void print();
	};

	struct AsmBinOpSub : Asm
	{
		uint8_t reg_dest;
		uint8_t reg_1;
		uint8_t reg_2;
		
		void build(std::vector<uint8_t> &bin);
		int size();
		void print();
	};

	struct AsmBinOpMul : Asm
	{
		uint8_t reg_dest;
		uint8_t reg_1;
		uint8_t reg_2;
		
		void build(std::vector<uint8_t> &bin);
		int size();
		void print();
	};

	struct AsmBinOpDiv : Asm
	{
		uint8_t reg_dest;
		uint8_t reg_1;
		uint8_t reg_2;
		
		void build(std::vector<uint8_t> &bin);
		int size();
		void print();
	};

	struct AsmBinOpMod : Asm
	{
		uint8_t reg_dest;
		uint8_t reg_1;
		uint8_t reg_2;
		
		void build(std::vector<uint8_t> &bin);
		int size();
		void print();
	};

	struct AsmBinOpGte : Asm
	{
		uint8_t reg_dest;
		uint8_t reg_1;
		uint8_t reg_2;
		
		void build(std::vector<uint8_t> &bin);
		int size();
		void print();
	};

	struct AsmBinOpLte : Asm
	{
		uint8_t reg_dest;
		uint8_t reg_1;
		uint8_t reg_2;
		
		void build(std::vector<uint8_t> &bin);
		int size();
		void print();
	};

	struct AsmBinOpEq : Asm
	{
		uint8_t reg_dest;
		uint8_t reg_1;
		uint8_t reg_2;
		
		void build(std::vector<uint8_t> &bin);
		int size();
		void print();
	};

	std::vector<Asm*> assembly(compiler::Node* root);
	std::vector<uint8_t> assemble(std::vector<Asm*> &bin);
}

#endif
