#include "nodes/nodes_if.hpp"
#include "asm/environment.hpp"

void compiler::NodeIf::asm_build(Environment &env, std::vector<Asm*> &bin)
{
	env.push_depth();
	this->expr->asm_build(env, bin);

	auto dest = env.get_last_reg();

	std::vector<Asm*> asm_true;
	this->true_stmt->asm_build(env, asm_true);
	uint8_t true_skip = 0;
	for (auto &cmd : asm_true)
		true_skip += cmd->size();

	if (this->false_stmt == nullptr)
	{
		auto cmd = new AsmJE();
		cmd->reg = dest;
		cmd->n = true_skip;

		bin.push_back(cmd);
		bin.insert(bin.end(), asm_true.begin(), asm_true.end());
	}
	else
	{
		std::vector<Asm*> asm_false;
		this->false_stmt->asm_build(env, asm_false);
		uint8_t false_skip = 0;
		for (auto &cmd : asm_false)
			false_skip += cmd->size();

		auto cmd_skip = new AsmSkip();
		cmd_skip->n = false_skip;
		true_skip += cmd_skip->size();

		auto cmd = new AsmJE();
		cmd->reg = dest;
		cmd->n = true_skip;

		bin.push_back(cmd);
		bin.insert(bin.end(), asm_true.begin(), asm_true.end());
		bin.push_back(cmd_skip);
		bin.insert(bin.end(), asm_false.begin(), asm_false.end());
	}

	env.pop_depth();
}
