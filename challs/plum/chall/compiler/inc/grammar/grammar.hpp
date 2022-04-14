#ifndef DCTF_GRAMMAR_HPP
#define DCTF_GRAMMAR_HPP

#include <iostream>
#include <vector>
#include <queue>
#include <string>

#include "tokenizer/tokenizer.hpp"
#include "nodes/nodes.hpp"
#include "grammar/grammar_terminal.hpp"
#include "grammar/grammar_stmt.hpp"
#include "grammar/grammar_if.hpp"
#include "grammar/grammar_expr.hpp"

namespace compiler
{
	Node* grammar(std::vector<Token>);
}

#endif
