#include "asm/asm.hpp"

void compiler::AsmString::print()
{
	std::cout << "AsmString ";
	for (auto it : string)
		std::cout
			<< std::setw(2)
			<< std::setfill('0')
			<< std::hex
			<< (int)it
			<< std::dec;
	std::cout << std::endl;
}

void compiler::AsmSkip::print()
{
	std::cout
		<< "AsmSkip n:" << (int)this->n
		<< std::endl;
}

void compiler::AsmJE::print()
{
	std::cout
		<< "AsmJE reg:" << (int)this->reg
		<< " n:" << (int)this->n
		<< std::endl;
}

void compiler::AsmRead::print()
{
	std::cout
		<< "AsmRead reg:" << (int)this->reg
		<< std::endl;
}

void compiler::AsmPrint::print()
{
	std::cout
		<< "AsmPrint i:" << (int)this->i
		<< std::endl;
}

void compiler::AsmMangle::print()
{
	std::cout
		<< "AsmMangle"
		<< std::endl;
}

void compiler::AsmReghash::print()
{
	std::cout
		<< "AsmReghash"
		<< std::endl;
}

void compiler::AsmExit::print()
{
	std::cout
		<< "AsmExit"
		<< std::endl;
}

void compiler::AsmLoad::print()
{
	std::cout
		<< "AsmLoad reg:" << (int)(this->reg)
		<< " val:" << (int)(this->val)
		<< std::endl;
}

void compiler::AsmBinOpAdd::print()
{
	std::cout
		<< "AsmBinOpAdd dest:" << (int)this->reg_dest
		<< " reg_1:" << (int)this->reg_1
		<< " reg_2:" << (int)this->reg_2
		<< std::endl;
}

void compiler::AsmBinOpSub::print()
{
	std::cout
		<< "AsmBinOpSub dest:" << (int)this->reg_dest
		<< " reg_1:" << (int)this->reg_1
		<< " reg_2:" << (int)this->reg_2
		<< std::endl;
}

void compiler::AsmBinOpMul::print()
{
	std::cout
		<< "AsmBinOpMul dest:" << (int)this->reg_dest
		<< " reg_1:" << (int)this->reg_1
		<< " reg_2:" << (int)this->reg_2
		<< std::endl;
}

void compiler::AsmBinOpDiv::print()
{
	std::cout
		<< "AsmBinOpDiv dest:" << (int)this->reg_dest
		<< " reg_1:" << (int)this->reg_1
		<< " reg_2:" << (int)this->reg_2
		<< std::endl;
}

void compiler::AsmBinOpMod::print()
{
	std::cout
		<< "AsmBinMod dest:" << (int)this->reg_dest
		<< " reg_1:" << (int)this->reg_1
		<< " reg_2:" << (int)this->reg_2
		<< std::endl;
}

void compiler::AsmBinOpGte::print()
{
	std::cout
		<< "AsmBinOpGte dest:" << (int)this->reg_dest
		<< " reg_1:" << (int)this->reg_1
		<< " reg_2:" << (int)this->reg_2
		<< std::endl;
}

void compiler::AsmBinOpLte::print()
{
	std::cout
		<< "AsmBinOpLte dest:" << (int)this->reg_dest
		<< " reg_1:" << (int)this->reg_1
		<< " reg_2:" << (int)this->reg_2
		<< std::endl;
}

void compiler::AsmBinOpEq::print()
{
	std::cout
		<< "AsmBinOpEq dest:" << (int)this->reg_dest
		<< " reg_1:" << (int)this->reg_1
		<< " reg_2:" << (int)this->reg_2
		<< std::endl;
}
