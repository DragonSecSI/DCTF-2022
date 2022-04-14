#include "grammar/grammar_if.hpp"

compiler::NodeIf* compiler::grammar_if(std::queue<Token> &tokens)
{
	auto key_token = tokens.front();
	if (key_token.type != Tokentype::alphanum || key_token.value != "if")
		throw std::runtime_error(std::string("Bad if key: ") + key_token.value);
	tokens.pop();

	auto node = new NodeIf();
	node->expr = grammar_expr(tokens);
	node->true_stmt = grammar_stmt(tokens);

	key_token = tokens.front();
	if (key_token.type == Tokentype::alphanum && key_token.value == "else")
	{
		tokens.pop();
		node->false_stmt = grammar_stmt(tokens);
	}

	return node;
}
