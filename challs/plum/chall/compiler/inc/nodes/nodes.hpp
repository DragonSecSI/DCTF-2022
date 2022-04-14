#ifndef DCTF_NODES_HPP
#define DCTF_NODES_HPP

#include <string>
#include <vector>
#include <memory>

#include "asm/asm.hpp"
#include "asm/environment.hpp"

namespace compiler
{
	struct Node
	{
		virtual void asm_build(Environment &env, std::vector<Asm*> &bin) = 0;
		virtual std::string print() = 0;
	};
}

#include "nodes/nodes_terminal.hpp"
#include "nodes/nodes_stmt.hpp"
#include "nodes/nodes_expr.hpp"
#include "nodes/nodes_if.hpp"

#endif
