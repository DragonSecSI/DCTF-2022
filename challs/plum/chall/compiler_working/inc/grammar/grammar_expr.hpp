#ifndef DCTF_GRAMMAR_EXPR_HPP
#define DCTF_GRAMMAR_EXPR_HPP

#include <iostream>
#include <queue>
#include <string>
#include <stdexcept>

#include "tokenizer/tokenizer.hpp"
#include "nodes/nodes.hpp"
#include "grammar/grammar.hpp"

namespace compiler
{
	NodeExpr* grammar_expr(std::queue<Token> &tokens);
	NodeExpr* grammar_expr_cmp(std::queue<Token> &tokens);
	NodeExpr* grammar_expr_l0(std::queue<Token> &tokens);
	NodeExpr* grammar_expr_l1(std::queue<Token> &tokens);
	NodeExpr* grammar_expr_l2(std::queue<Token> &tokens);
	NodeExpr* grammar_expr_l3(std::queue<Token> &tokens);
	NodeExpr* grammar_expr_read(std::queue<Token> &tokens);
}

#endif
