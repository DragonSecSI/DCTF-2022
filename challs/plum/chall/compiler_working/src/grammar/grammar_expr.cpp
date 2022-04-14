#include "grammar/grammar_expr.hpp"

compiler::NodeExpr* compiler::grammar_expr(std::queue<Token> &tokens)
{
	auto lb_token = tokens.front();
	if (lb_token.type != Tokentype::symbol || lb_token.value != "(")
		throw std::runtime_error("Missing left bracket");
	tokens.pop();

	auto node = grammar_expr_cmp(tokens);

	auto rb_token = tokens.front();
	if (rb_token.type != Tokentype::symbol || rb_token.value != ")")
		throw std::runtime_error("Missing right bracket");
	tokens.pop();

	return node;
}

compiler::NodeExpr* compiler::grammar_expr_cmp(std::queue<Token> &tokens)
{
	auto left = grammar_expr_l0(tokens);

	auto token = tokens.front();
	if (token.type != Tokentype::symbol)
		throw std::runtime_error(std::string("Comparator is not of type symbol: ") + token.value);
	if (token.value == "<=")
	{
		tokens.pop();
		auto node = new NodeExprLte();
		node->left = left;
		node->right = grammar_expr_l0(tokens);
		return node;
	}
	else if (token.value == ">=")
	{
		tokens.pop();
		auto node = new NodeExprGte();
		node->left = left;
		node->right = grammar_expr_l0(tokens);
		return node;
	}
	else if (token.value == "==")
	{
		tokens.pop();
		auto node = new NodeExprEq();
		node->left = left;
		node->right = grammar_expr_l0(tokens);
		return node;
	}

	throw std::runtime_error(std::string("Invalid comparator symbol: ") + token.value);
}

compiler::NodeExpr* compiler::grammar_expr_l0(std::queue<Token> &tokens)
{
	auto expr = grammar_expr_l1(tokens);
	while (true)
	{
		auto token = tokens.front();
		if (token.type == Tokentype::symbol && token.value == "+")
		{
			tokens.pop();
			auto tmp = new NodeExprAdd();
			tmp->left = expr;
			tmp->right = grammar_expr_l1(tokens);
			expr = tmp;
		}
		else if (token.type == Tokentype::symbol && token.value == "-")
		{
			tokens.pop();
			auto tmp = new NodeExprSub();
			tmp->left = expr;
			tmp->right = grammar_expr_l1(tokens);
			expr = tmp;
		}
		else
		{
			break;
		}
	}
	return expr;
}

compiler::NodeExpr* compiler::grammar_expr_l1(std::queue<Token> &tokens)
{
	auto expr = grammar_expr_l2(tokens);
	while (true)
	{
		auto token = tokens.front();
		if (token.type == Tokentype::symbol && token.value == "*")
		{
			tokens.pop();
			auto tmp = new NodeExprMul();
			tmp->left = expr;
			tmp->right = grammar_expr_l2(tokens);
			expr = tmp;
		}
		else if (token.type == Tokentype::symbol && token.value == "/")
		{
			tokens.pop();
			auto tmp = new NodeExprDiv();
			tmp->left = expr;
			tmp->right = grammar_expr_l2(tokens);
			expr = tmp;
		}
		else
		{
			break;
		}
	}
	return expr;
}

compiler::NodeExpr* compiler::grammar_expr_l2(std::queue<Token> &tokens)
{
	auto expr = grammar_expr_l3(tokens);
	while (true)
	{
		auto token = tokens.front();
		if (token.type == Tokentype::symbol && token.value == "%")
		{
			tokens.pop();
			auto tmp = new NodeExprSub();
			tmp->left = expr;
			tmp->right = grammar_expr_l3(tokens);
			expr = tmp;
		}
		else
		{
			break;
		}
	}
	return expr;
}

compiler::NodeExpr* compiler::grammar_expr_l3(std::queue<Token> &tokens)
{
	auto token = tokens.front();
	if (token.type == Tokentype::symbol && token.value == "(")
	{
		tokens.pop();
		auto expr = grammar_expr_l0(tokens);
		token = tokens.front();
		if (token.type != Tokentype::symbol || token.value != ")")
			throw std::runtime_error(std::string("Expected right bracket, got: ") + token.value);
		tokens.pop();
		return expr;
	}
	else if (token.type == Tokentype::digit)
	{
		tokens.pop();
		auto expr = new NodeExprTerm();
		expr->value = stoi(token.value);
		return expr;
	}
	else if (token.type == Tokentype::alphanum && token.value == "read")
	{
		return grammar_expr_read(tokens);
	}

	throw std::runtime_error(std::string("Bad expression terminal: ") + token.value);
}

compiler::NodeExpr* compiler::grammar_expr_read(std::queue<Token> &tokens)
{
	auto key_token = tokens.front();
	if (key_token.type != Tokentype::alphanum || key_token.value != "read")
		throw std::runtime_error(std::string("Bad read keyword: ") + key_token.value);
	tokens.pop();

	auto node = new NodeExprRead();
	return node;
}
