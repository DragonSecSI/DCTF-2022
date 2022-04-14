std::string compiler::NodeStmt::print()
{
	return
		std::string("(NodeStmt ") +
		this->stmt->print() +
		std::string(")");
}

std::string compiler::NodeStmts::print()
{
	std::string tail = "";
	if (this->next != nullptr)
		tail = this->next->print();
	return
		std::string("(NodeStmts ") +
		this->stmt->print() +
		tail +
		std::string(")");
}

std::string compiler::NodePrint::print()
{
	return
		std::string("(NodePrint ") +
		this->string->print() +
		std::string(")");
}

std::string compiler::NodeMangle::print()
{
	return std::string("(NodeMangle)");
}

std::string compiler::NodeReghash::print()
{
	return std::string("(NodeReghash)");
}

std::string compiler::NodeExit::print()
{
	return std::string("(NodeExit)");
}
