#include "grammar/grammar.hpp"

#include "grammar_expr.cpp"
#include "grammar_if.cpp"
#include "grammar_stmt.cpp"
#include "grammar_terminal.cpp"

compiler::Node* compiler::grammar(std::vector<Token> tokens_vec)
{
	std::queue<Token> tokens;
	for (auto token : tokens_vec)
		tokens.push(token);

	return grammar_stmts(tokens);
}
