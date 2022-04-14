#include "asm/asm.hpp"

int compiler::AsmString::size()
{
	return 2 + this->string.size();
}

int compiler::AsmSkip::size()
{
	return 2;
}

int compiler::AsmJE::size()
{
	return 3;
}

int compiler::AsmRead::size()
{
	return 2;
}

int compiler::AsmPrint::size()
{
	return 2;
}

int compiler::AsmMangle::size()
{
	return 1;
}

int compiler::AsmReghash::size()
{
	return 1;
}

int compiler::AsmExit::size()
{
	return 1;
}

int compiler::AsmLoad::size()
{
	return 3;
}

int compiler::AsmBinOpAdd::size()
{
	return 4;
}

int compiler::AsmBinOpSub::size()
{
	return 4;
}

int compiler::AsmBinOpMul::size()
{
	return 4;
}

int compiler::AsmBinOpDiv::size()
{
	return 4;
}

int compiler::AsmBinOpMod::size()
{
	return 4;
}

int compiler::AsmBinOpGte::size()
{
	return 4;
}

int compiler::AsmBinOpLte::size()
{
	return 4;
}

int compiler::AsmBinOpEq::size()
{
	return 4;
}
