#ifndef DCTF_GRAMMAR_STMT_HPP
#define DCTF_GRAMMAR_STMT_HPP

#include <iostream>
#include <queue>
#include <string>
#include <stdexcept>

#include "tokenizer/tokenizer.hpp"
#include "nodes/nodes.hpp"
#include "grammar/grammar.hpp"
#include "grammar/grammar_terminal.hpp"

namespace compiler
{
	NodeStmts* grammar_stmts(std::queue<Token> &tokens);
	NodeStmt* grammar_stmt(std::queue<Token> &tokens);
	NodePrint* grammar_print(std::queue<Token> &tokens);
	NodeMangle* grammar_mangle(std::queue<Token> &tokens);
	NodeReghash* grammar_reghash(std::queue<Token> &tokens);
	NodeExit* grammar_exit(std::queue<Token> &tokens);
}

#endif
