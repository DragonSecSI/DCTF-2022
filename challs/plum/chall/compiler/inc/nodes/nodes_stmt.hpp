#ifndef DCTF_NODES_STMT_HPP
#define DCTF_NODES_STMT_HPP

#include <string>

namespace compiler
{
	struct NodeStmt : Node
	{
		Node* stmt = nullptr;

		void asm_build(Environment &env, std::vector<Asm*> &bin);
		std::string print();
	};

	struct NodeStmts : Node
	{
		NodeStmt* stmt = nullptr;
		NodeStmts* next = nullptr;

		void asm_build(Environment &env, std::vector<Asm*> &bin);
		std::string print();
	};

	struct NodePrint : Node
	{
		NodeString* string = nullptr;

		void asm_build(Environment &env, std::vector<Asm*> &bin);
		std::string print();
	};

	struct NodeMangle : Node
	{
		void asm_build(Environment &env, std::vector<Asm*> &bin);
		std::string print();
	};

	struct NodeReghash : Node
	{
		void asm_build(Environment &env, std::vector<Asm*> &bin);
		std::string print();
	};

	struct NodeExit : Node
	{
		void asm_build(Environment &env, std::vector<Asm*> &bin);
		std::string print();
	};
}

#endif
