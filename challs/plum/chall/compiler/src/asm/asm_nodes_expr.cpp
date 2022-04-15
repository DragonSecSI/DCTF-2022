#include "nodes/nodes_expr.hpp"
#include "asm/environment.hpp"

void compiler::NodeExpr::asm_build(Environment &env, std::vector<Asm*> &bin)
{
	this->expr->asm_build(env, bin);
}

void compiler::NodeExprLte::asm_build(Environment &env, std::vector<Asm*> &bin)
{
	auto cmd = new AsmBinOpGte();
	cmd->reg_dest = env.get_reg();

	this->left->asm_build(env, bin);
	cmd->reg_1 = env.get_last_reg();

	this->right->asm_build(env, bin);
	cmd->reg_2 = env.get_last_reg();

	env.set_last_reg(cmd->reg_dest);
	bin.push_back(cmd);
}

void compiler::NodeExprGte::asm_build(Environment &env, std::vector<Asm*> &bin)
{
	auto cmd = new AsmBinOpLte();
	cmd->reg_dest = env.get_reg();

	this->left->asm_build(env, bin);
	cmd->reg_1 = env.get_last_reg();

	this->right->asm_build(env, bin);
	cmd->reg_2 = env.get_last_reg();

	env.set_last_reg(cmd->reg_dest);
	bin.push_back(cmd);
}

void compiler::NodeExprEq::asm_build(Environment &env, std::vector<Asm*> &bin)
{
	auto cmd = new AsmBinOpEq();
	cmd->reg_dest = env.get_reg();

	this->left->asm_build(env, bin);
	cmd->reg_1 = env.get_last_reg();

	this->right->asm_build(env, bin);
	cmd->reg_2 = env.get_last_reg();

	env.set_last_reg(cmd->reg_dest);
	bin.push_back(cmd);
}

void compiler::NodeExprAdd::asm_build(Environment &env, std::vector<Asm*> &bin)
{
	auto cmd = new AsmBinOpAdd();
	cmd->reg_dest = env.get_reg();

	this->left->asm_build(env, bin);
	cmd->reg_1 = env.get_last_reg();

	this->right->asm_build(env, bin);
	cmd->reg_2 = env.get_last_reg();

	env.set_last_reg(cmd->reg_dest);
	bin.push_back(cmd);
}

void compiler::NodeExprSub::asm_build(Environment &env, std::vector<Asm*> &bin)
{
	auto cmd = new AsmBinOpSub();
	cmd->reg_dest = env.get_reg();

	this->left->asm_build(env, bin);
	cmd->reg_1 = env.get_last_reg();

	this->right->asm_build(env, bin);
	cmd->reg_2 = env.get_last_reg();

	env.set_last_reg(cmd->reg_dest);
	bin.push_back(cmd);
}

void compiler::NodeExprMul::asm_build(Environment &env, std::vector<Asm*> &bin)
{
	auto cmd = new AsmBinOpMul();
	cmd->reg_dest = env.get_reg();

	this->left->asm_build(env, bin);
	cmd->reg_1 = env.get_last_reg();

	this->right->asm_build(env, bin);
	cmd->reg_2 = env.get_last_reg();

	env.set_last_reg(cmd->reg_dest);
	bin.push_back(cmd);
}

void compiler::NodeExprDiv::asm_build(Environment &env, std::vector<Asm*> &bin)
{
	auto cmd = new AsmBinOpDiv();
	cmd->reg_dest = env.get_reg();

	this->left->asm_build(env, bin);
	cmd->reg_2 = env.get_last_reg();

	this->right->asm_build(env, bin);
	cmd->reg_1 = env.get_last_reg();

	env.set_last_reg(cmd->reg_dest);
	bin.push_back(cmd);
}

void compiler::NodeExprMod::asm_build(Environment &env, std::vector<Asm*> &bin)
{
	auto cmd = new AsmBinOpMod();
	cmd->reg_dest = env.get_reg();

	this->left->asm_build(env, bin);
	cmd->reg_1 = env.get_last_reg();

	this->right->asm_build(env, bin);
	cmd->reg_2 = env.get_last_reg();

	env.set_last_reg(cmd->reg_dest);
	bin.push_back(cmd);
}

void compiler::NodeExprTerm::asm_build(Environment &env, std::vector<Asm*> &bin)
{
	auto cmd = new AsmLoad();
	cmd->reg = env.get_reg();
	cmd->val = this->value;

	env.set_last_reg(cmd->reg);
	bin.push_back(cmd);
}

void compiler::NodeExprRead::asm_build(Environment &env, std::vector<Asm*> &bin)
{
	auto cmd = new AsmRead();
	cmd->reg = env.get_reg();

	env.set_last_reg(cmd->reg);
	bin.push_back(cmd);
}
