#ifndef DCTF_NODES_TERMINAL_HPP
#define DCTF_NODES_TERMINAL_HPP

#include <string>
#include <sstream>

#include "nodes/nodes.hpp"

namespace compiler
{
	struct NodeDigit : Node
	{
		int value;

		void asm_build(Environment &env, std::vector<Asm*> &bin);
		std::string print();
	};

	struct NodeString : Node
	{
		std::string value;

		void asm_build(Environment &env, std::vector<Asm*> &bin);
		std::string print();
	};

	struct NodeSymbol : Node
	{
		std::string value;

		void asm_build(Environment &env, std::vector<Asm*> &bin);
		std::string print();
	};
}

#endif
