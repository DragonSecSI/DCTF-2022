#include "grammar/grammar_stmt.hpp"

compiler::NodeStmts* compiler::grammar_stmts(std::queue<Token> &tokens)
{
	auto head = new NodeStmts();
	auto tmp = head;

	while (true)
	{
		tmp->stmt = grammar_stmt(tokens);
		if (tokens.empty())
			break;

		tmp->next = new NodeStmts();
		tmp = tmp->next;
	}

	return head;
}

compiler::NodeStmt* compiler::grammar_stmt(std::queue<Token> &tokens)
{
	auto token = tokens.front();
	if (token.type != Tokentype::alphanum)
		throw std::runtime_error(std::string("Bad statement token type: ") + token.value);

	auto node = new NodeStmt();
	if (token.value == "print")
		node->stmt = grammar_print(tokens);
	else if (token.value == "mangle")
		node->stmt = grammar_mangle(tokens);
	else if (token.value == "reghash")
		node->stmt = grammar_reghash(tokens);
	else if (token.value == "exit")
		node->stmt = grammar_exit(tokens);
	else if (token.value == "if")
		node->stmt = grammar_if(tokens);
	else
		throw std::runtime_error(std::string("Bad statement token: ") + token.value);

	return node;
}

compiler::NodePrint* compiler::grammar_print(std::queue<Token> &tokens)
{
	auto key_token = tokens.front();
	if (key_token.type != Tokentype::alphanum || key_token.value != "print")
		throw std::runtime_error(std::string("Bad print keyword: ") + key_token.value);
	tokens.pop();

	auto node = new NodePrint();
	node->string = grammar_terminal_string(tokens);
	return node;
}

compiler::NodeMangle* compiler::grammar_mangle(std::queue<Token> &tokens)
{
	auto key_token = tokens.front();
	if (key_token.type != Tokentype::alphanum || key_token.value != "mangle")
		throw std::runtime_error(std::string("Bad mangle keyword: ") + key_token.value);
	tokens.pop();

	auto node = new NodeMangle();
	return node;
}

compiler::NodeReghash* compiler::grammar_reghash(std::queue<Token> &tokens)
{
	auto key_token = tokens.front();
	if (key_token.type != Tokentype::alphanum || key_token.value != "reghash")
		throw std::runtime_error(std::string("Bad reghash keyword: ") + key_token.value);
	tokens.pop();

	auto node = new NodeReghash();
	return node;
}

compiler::NodeExit* compiler::grammar_exit(std::queue<Token> &tokens)
{
	auto key_token = tokens.front();
	if (key_token.type != Tokentype::alphanum || key_token.value != "exit")
		throw std::runtime_error(std::string("Bad exit keyword: ") + key_token.value);
	tokens.pop();

	auto node = new NodeExit();
	return node;
}
