#ifndef DCTF_NODES_IF_HPP
#define DCTF_NODES_IF_HPP

#include <string>

#include "nodes/nodes.hpp"

namespace compiler
{
	struct NodeIf : Node
	{
		NodeExpr* expr = nullptr;
		NodeStmt* true_stmt = nullptr;
		NodeStmt* false_stmt = nullptr;

		void asm_build(Environment &env, std::vector<Asm*> &bin);
		std::string print();
	};
}

#endif

