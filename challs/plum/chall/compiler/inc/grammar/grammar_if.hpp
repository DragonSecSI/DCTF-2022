#ifndef DCTF_GRAMMAR_IF_HPP
#define DCTF_GRAMMAR_IF_HPP

#include <iostream>
#include <queue>
#include <string>
#include <stdexcept>

#include "tokenizer/tokenizer.hpp"
#include "nodes/nodes.hpp"
#include "grammar/grammar.hpp"
#include "grammar/grammar_stmt.hpp"
#include "grammar/grammar_expr.hpp"

namespace compiler
{
	NodeIf* grammar_if(std::queue<Token> &tokens);
}

#endif
