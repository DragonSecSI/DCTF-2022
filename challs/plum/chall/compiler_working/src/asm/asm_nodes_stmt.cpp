#include "nodes/nodes_stmt.hpp"
#include "asm/environment.hpp"

void compiler::NodeStmts::asm_build(Environment &env, std::vector<Asm*> &bin)
{
	auto node = this;
	while (node != nullptr)
	{
		node->stmt->asm_build(env, bin);
		node = node->next;
	}
}

void compiler::NodeStmt::asm_build(Environment &env, std::vector<Asm*> &bin)
{
	this->stmt->asm_build(env, bin);
}

void compiler::NodePrint::asm_build(Environment &env, std::vector<Asm*> &bin)
{
	int string_index = env.add_string(this->string->value);

	auto cmd = new AsmPrint();
	cmd->i = string_index;
	bin.push_back(cmd);
}

void compiler::NodeMangle::asm_build(Environment &env, std::vector<Asm*> &bin)
{
	auto cmd = new AsmMangle();
	bin.push_back(cmd);
}

void compiler::NodeReghash::asm_build(Environment &env, std::vector<Asm*> &bin)
{
	auto cmd = new AsmReghash();
	bin.push_back(cmd);
}

void compiler::NodeExit::asm_build(Environment &env, std::vector<Asm*> &bin)
{
	auto cmd = new AsmExit();
	bin.push_back(cmd);
}
