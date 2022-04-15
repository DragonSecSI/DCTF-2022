#include "grammar/grammar_terminal.hpp"

compiler::NodeDigit* compiler::grammar_terminal_digit(std::queue<Token> &tokens)
{
	auto token = tokens.front();
	if (token.type != Tokentype::digit)
		throw std::runtime_error(std::string("Bad digit type: ") + token.value);
	tokens.pop();

	auto node = new NodeDigit();
	node->value = stoi(token.value);
	return node;
}

compiler::NodeString* compiler::grammar_terminal_string(std::queue<Token> &tokens)
{
	auto token = tokens.front();
	if (token.type != Tokentype::string)
		throw std::runtime_error(std::string("Bad string type: ") + token.value);
	tokens.pop();

	auto node = new NodeString();
	node->value = token.value;
	return node;
}

compiler::NodeSymbol* compiler::grammar_terminal_symbol(std::queue<Token> &tokens)
{
	auto token = tokens.front();
	if (token.type != Tokentype::symbol)
		throw std::runtime_error(std::string("Bad symbol type: ") + token.value);
	tokens.pop();

	auto node = new NodeSymbol();
	node->value = token.value;
	return node;
}
