#include <stdexcept>

#include "nodes/nodes_terminal.hpp"
#include "asm/environment.hpp"

void compiler::NodeDigit::asm_build(Environment &env, std::vector<Asm*> &bin)
{
	throw std::runtime_error("asm_build can't run on NodeDigit.");
}

void compiler::NodeString::asm_build(Environment &env, std::vector<Asm*> &bin)
{
	throw std::runtime_error("asm_build can't run on NodeString.");
}

void compiler::NodeSymbol::asm_build(Environment &env, std::vector<Asm*> &bin)
{
	throw std::runtime_error("asm_build can't run on NodeSymbol.");
}
