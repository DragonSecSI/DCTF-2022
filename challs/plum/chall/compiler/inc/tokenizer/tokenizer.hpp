#ifndef DCTF_TOKENIZER_HPP
#define DCTF_TOKENIZER_HPP

#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <stdexcept>

namespace compiler
{

	enum class State
	{
		normal,
		string,
		stringescape,
	};

	enum class Tokentype
	{
		none,
		alphanum,
		digit,
		symbol,
		string,
	};

	struct Token
	{
		Tokentype type;
		std::string value;

		Token(Tokentype type, std::string value)
		{
			this->type = type;
			this->value = value;
		}
	};

	std::vector<Token> tokenizer(std::string);

}

#endif
