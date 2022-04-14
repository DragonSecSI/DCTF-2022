#ifndef DCTF_GRAMMAR_TERMINAL_HPP
#define DCTF_GRAMMAR_TERMINAL_HPP

#include <iostream>
#include <queue>
#include <string>
#include <sstream>
#include <stdexcept>

#include "tokenizer/tokenizer.hpp"
#include "nodes/nodes.hpp"
#include "grammar/grammar.hpp"

namespace compiler
{
	NodeDigit* grammar_terminal_digit(std::queue<Token> &tokens);
	NodeString* grammar_terminal_string(std::queue<Token> &tokens);
	NodeSymbol* grammar_terminal_symbol(std::queue<Token> &tokens);
}

#endif

