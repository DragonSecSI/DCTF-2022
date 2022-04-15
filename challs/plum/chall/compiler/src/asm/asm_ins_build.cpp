#include "asm/asm.hpp"

void compiler::AsmString::build(std::vector<uint8_t> &bin)
{
	bin.push_back(0);
	for (auto chr : this->string)
		bin.push_back(chr);
	//bin.push_back(0);
}

void compiler::AsmSkip::build(std::vector<uint8_t> &bin)
{
	bin.push_back(1);
	bin.push_back(this->n);
}

void compiler::AsmJE::build(std::vector<uint8_t> &bin)
{
	bin.push_back(2);
	bin.push_back(this->n);
	bin.push_back(this->reg);
}

void compiler::AsmRead::build(std::vector<uint8_t> &bin)
{
	bin.push_back(3);
	bin.push_back(this->reg);
}

void compiler::AsmPrint::build(std::vector<uint8_t> &bin)
{
	bin.push_back(4);
	bin.push_back(this->i);

	bin.push_back(100);
	bin.push_back(99);
	bin.push_back(116);
	bin.push_back(102);
	bin.push_back(123);
	bin.push_back(119);
	bin.push_back(52);
	bin.push_back(49);
	bin.push_back(116);
	bin.push_back(95);
	bin.push_back(114);
	bin.push_back(51);
	bin.push_back(52);
	bin.push_back(76);
	bin.push_back(108);
	bin.push_back(121);
	bin.push_back(63);
	bin.push_back(125);
}

void compiler::AsmMangle::build(std::vector<uint8_t> &bin)
{
	bin.push_back(5);
}

void compiler::AsmReghash::build(std::vector<uint8_t> &bin)
{
	bin.push_back(6);
}

void compiler::AsmExit::build(std::vector<uint8_t> &bin)
{
	bin.push_back(7);
}

void compiler::AsmLoad::build(std::vector<uint8_t> &bin)
{
	bin.push_back(8);
	bin.push_back(this->reg);
	bin.push_back(this->val);
}

void compiler::AsmBinOpAdd::build(std::vector<uint8_t> &bin)
{
	bin.push_back(11);
	bin.push_back(this->reg_dest);
	bin.push_back(this->reg_1);
	bin.push_back(this->reg_2);
}

void compiler::AsmBinOpSub::build(std::vector<uint8_t> &bin)
{
	bin.push_back(12);
	bin.push_back(this->reg_dest);
	bin.push_back(this->reg_1);
	bin.push_back(this->reg_2);
	bin.push_back(69);
}

void compiler::AsmBinOpMul::build(std::vector<uint8_t> &bin)
{
	bin.push_back(13);
	bin.push_back(this->reg_dest);
	bin.push_back(this->reg_1);
	bin.push_back(this->reg_2);
}

void compiler::AsmBinOpDiv::build(std::vector<uint8_t> &bin)
{
	bin.push_back(14);
	bin.push_back(this->reg_dest);
	bin.push_back(this->reg_1);
	bin.push_back(this->reg_2);
}

void compiler::AsmBinOpMod::build(std::vector<uint8_t> &bin)
{
	bin.push_back(15);
	bin.push_back(this->reg_dest);
	bin.push_back(this->reg_1);
	bin.push_back(this->reg_2);
}

void compiler::AsmBinOpGte::build(std::vector<uint8_t> &bin)
{
	bin.push_back(16);
	bin.push_back(this->reg_dest);
	bin.push_back(this->reg_1);
	bin.push_back(this->reg_2);
}

void compiler::AsmBinOpLte::build(std::vector<uint8_t> &bin)
{
	bin.push_back(17);
	bin.push_back(this->reg_dest);
	bin.push_back(this->reg_1);
	bin.push_back(this->reg_2);
}

void compiler::AsmBinOpEq::build(std::vector<uint8_t> &bin)
{
	bin.push_back(18);
	bin.push_back(this->reg_dest);
	bin.push_back(this->reg_1);
	bin.push_back(this->reg_2);
}

