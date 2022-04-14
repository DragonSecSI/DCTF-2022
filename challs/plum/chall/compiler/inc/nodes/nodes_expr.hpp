#ifndef DCTF_NODES_EXPR_HPP
#define DCTF_NODES_EXPR_HPP

#include <string>
#include <sstream>

namespace compiler
{
	struct NodeExpr : Node
	{
		NodeExpr* expr;

		void asm_build(Environment &env, std::vector<Asm*> &bin);
		std::string print();
	};

	struct NodeExprLte : NodeExpr
	{
		NodeExpr *left;
		NodeExpr *right;

		void asm_build(Environment &env, std::vector<Asm*> &bin);
		std::string print();
	};

	struct NodeExprGte : NodeExpr
	{
		NodeExpr *left;
		NodeExpr *right;

		void asm_build(Environment &env, std::vector<Asm*> &bin);
		std::string print();
	};

	struct NodeExprEq : NodeExpr
	{
		NodeExpr *left;
		NodeExpr *right;

		void asm_build(Environment &env, std::vector<Asm*> &bin);
		std::string print();
	};

	struct NodeExprAdd : NodeExpr
	{
		NodeExpr *left;
		NodeExpr *right;

		void asm_build(Environment &env, std::vector<Asm*> &bin);
		std::string print();
	};

	struct NodeExprSub : NodeExpr
	{
		NodeExpr *left;
		NodeExpr *right;

		void asm_build(Environment &env, std::vector<Asm*> &bin);
		std::string print();
	};

	struct NodeExprMul : NodeExpr
	{
		NodeExpr *left;
		NodeExpr *right;

		void asm_build(Environment &env, std::vector<Asm*> &bin);
		std::string print();
	};

	struct NodeExprDiv : NodeExpr
	{
		NodeExpr *left;
		NodeExpr *right;

		void asm_build(Environment &env, std::vector<Asm*> &bin);
		std::string print();
	};

	struct NodeExprMod : NodeExpr
	{
		NodeExpr *left;
		NodeExpr *right;

		void asm_build(Environment &env, std::vector<Asm*> &bin);
		std::string print();
	};

	struct NodeExprTerm : NodeExpr
	{
		int value;

		void asm_build(Environment &env, std::vector<Asm*> &bin);
		std::string print();
	};

	struct NodeExprRead : NodeExpr
	{
		void asm_build(Environment &env, std::vector<Asm*> &bin);
		std::string print();
	};
}

#endif
