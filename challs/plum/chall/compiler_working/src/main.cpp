#include "main.hpp"

const bool debug = false;

int main(int argc, char* argv[])
{
	if (argc != 3) {
		std::cerr
			<< "Usage: "
			<< argv[0]
			<< " <input file> <output file>"
			<< std::endl;
		return 1;
	}

	std::ifstream source_file(argv[1]);
	if (!source_file.is_open())
	{
		std::cerr << "Could not open source file" << std::endl;
		return 2;
	}

	std::ofstream destination_file(argv[2], std::ios::binary | std::ios::out);
	if (!destination_file.is_open())
	{
		std::cerr << "Could not open output file" << std::endl;
		return 3;
	}

	std::stringstream source;
	source << source_file.rdbuf();

	auto tokens = compiler::tokenizer(source.str());
	if (debug)
	{
		std::cout << "[DEBUG] Tokenizer" << std::endl;
		for (auto token : tokens)
		{
			std::cout
				<< (int)token.type
				<< ": "
				<< token.value
				<< std::endl;
		}
	}

	auto node = compiler::grammar(tokens);
	if (debug)
	{
		std::cout << "[DEBUG] Grammar" << std::endl;
		std::cout << node->print() << std::endl;
	}

	auto asm_cmds = compiler::assembly(node);
	if (debug)
	{
		std::cout << "[DEBUG] Asm" << std::endl;
		for (auto it : asm_cmds)
		{
			it->print();
		}
	}

	auto bin = compiler::assemble(asm_cmds);
	for (uint8_t byte : bin)
	{
		destination_file.write((const char *)&byte, sizeof(uint8_t));
	}

	return 0;
}
