#include "nodes/nodes_expr.hpp"

std::string compiler::NodeExpr::print()
{
	return
		std::string("(NodeExpr ") +
		this->expr->print() +
		std::string(")");
}

std::string compiler::NodeExprLte::print()
{
	return
		std::string("(NodeExprLte ") +
		this->left->print() + " " +
		this->right->print() +
		std::string(")");
}

std::string compiler::NodeExprGte::print()
{
	return
		std::string("(NodeExprGte ") +
		this->left->print() + " " +
		this->right->print() +
		std::string(")");
}

std::string compiler::NodeExprEq::print()
{
	return
		std::string("(NodeExprEq ") +
		this->left->print() + " " +
		this->right->print() +
		std::string(")");
}

std::string compiler::NodeExprAdd::print()
{
	return
		std::string("(NodeExprAdd ") +
		this->left->print() + " " +
		this->right->print() +
		std::string(")");
}

std::string compiler::NodeExprSub::print()
{
	return
		std::string("(NodeExprSub ") +
		this->left->print() + " " +
		this->right->print() +
		std::string(")");
}

std::string compiler::NodeExprMul::print()
{
	return
		std::string("(NodeExprMul ") +
		this->left->print() + " " +
		this->right->print() +
		std::string(")");
}

std::string compiler::NodeExprDiv::print()
{
	return
		std::string("(NodeExprDiv ") +
		this->left->print() + " " +
		this->right->print() +
		std::string(")");
}

std::string compiler::NodeExprMod::print()
{
	return
		std::string("(NodeExprMod ") +
		this->left->print() + " " +
		this->right->print() +
		std::string(")");
}

std::string compiler::NodeExprTerm::print()
{
	std::stringstream ss;
	ss
		<< "(NodeExprTerm "
		<< this->value
		<< ")";
	return ss.str();
}

std::string compiler::NodeExprRead::print()
{
	return std::string("(NodeRead)");
}

