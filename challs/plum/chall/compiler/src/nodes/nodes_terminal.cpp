#include "nodes/nodes.hpp"

std::string compiler::NodeDigit::print()
{
	std::stringstream ss;
	ss
		<< "(NodeDigit "
		<< this->value
		<< ")";
	return ss.str();
}

std::string compiler::NodeString::print()
{
	return
		std::string("(NodeString \"") +
		this->value +
		std::string("\")");
}

std::string compiler::NodeSymbol::print()
{
	return
		std::string("(NodeSymbol ") +
		this->value +
		std::string(")");
}
