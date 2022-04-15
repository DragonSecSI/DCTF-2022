#include "asm/environment.hpp"

int compiler::Environment::add_string(std::string str)
{
	int i = this->strings.size();
	this->strings.push_back(str);
	return i;
}

std::vector<std::string> compiler::Environment::get_strings()
{
	return this->strings;
}

int compiler::Environment::get_reg()
{
	int i = this->reg_counter;
	this->reg_counter++;
	return i;
}

void compiler::Environment::push_depth()
{
	this->depth++;
}

void compiler::Environment::pop_depth()
{
	this->depth--;
	if (this->depth == 0)
		this->reg_counter = 1;
}

uint8_t compiler::Environment::get_last_reg()
{
	return this->last_reg;
}

void compiler::Environment::set_last_reg(uint8_t reg)
{
	this->last_reg = reg;
}
