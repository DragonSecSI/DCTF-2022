#include "asm/asm.hpp"
#include "asm/asm_impl.hpp"

#include "environment.cpp"
#include "asm_ins_print.cpp"
#include "asm_ins_size.cpp"
#include "asm_ins_build.cpp"
#include "asm_nodes.cpp"

std::vector<compiler::Asm*> compiler::assembly(Node* root)
{
	Environment env;
	std::vector<Asm*> bin;

	root->asm_build(env, bin);

	std::vector<Asm*> new_bin;
	auto strings = env.get_strings();
	for (auto &str : strings)
	{
		auto cmd = new AsmString();
		for (auto chr : str)
			cmd->string.push_back(chr);
		new_bin.push_back(cmd);
	}

	new_bin.insert(new_bin.end(), bin.begin(), bin.end());

	return new_bin;
}

std::vector<uint8_t> compiler::assemble(std::vector<Asm*> &bin)
{
	std::vector<uint8_t> out;
	for (auto cmd : bin)
		cmd->build(out);
	return out;
}
