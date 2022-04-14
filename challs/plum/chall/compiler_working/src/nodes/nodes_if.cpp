#include "nodes/nodes_if.hpp"

std::string compiler::NodeIf::print()
{
	std::string tail = "";
	if (false_stmt != nullptr)
		tail = this->false_stmt->print();
	return
		std::string("(NodeIf ") +
		this->expr->print() + " " +
		this->true_stmt->print() + " " +
		tail +
		std::string(")");
}
