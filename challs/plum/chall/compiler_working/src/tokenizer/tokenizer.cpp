#include "tokenizer/tokenizer.hpp"

std::vector<compiler::Token> compiler::tokenizer(std::string data)
{
	std::vector<Token> tokens;

	State state = State::normal;
	Tokentype type = Tokentype::none;
	std::string tmp = "";
	for (char c : data + std::string(" "))
	{
		if (state == State::normal)
		{
			if (c >= '0' && c <= '9')
			{
				if (type == Tokentype::symbol)
				{
					tokens.push_back(Token(type, tmp));
					tmp = "";
					type = Tokentype::digit;
				}
				else if (type == Tokentype::none)
					type = Tokentype::digit;
				tmp += c;
			}
			else if (c >= 'a' && c <= 'z')
			{
				if (type == Tokentype::digit)
				{
					throw std::runtime_error("Invalid token");
				}
				else if (type == Tokentype::symbol)
				{
					tokens.push_back(Token(type, tmp));
					tmp = "";
				}
				type = Tokentype::alphanum;
				tmp += c;
			}
			else if (c == '(' || c == ')' || c == '-' || c == '+' || c == '*' || c == '/' || c == '%')
			{
				if (type != Tokentype::none)
				{
					tokens.push_back(Token(type, tmp));
				}

				tokens.push_back(Token(Tokentype::symbol, std::string(1, c)));

				type = Tokentype::none;
				tmp = "";
			}
			else if (c == '<' || c == '>' || c == '=')
			{
				if (type == Tokentype::digit)
				{
					tokens.push_back(Token(type, tmp));
					tmp = "";
				}
				else if (type == Tokentype::alphanum)
				{
					tokens.push_back(Token(type, tmp));
					tmp = "";
				}
				if (type == Tokentype::string)
				{
					tokens.push_back(Token(type, tmp));
					tmp = "";
				}
				type = Tokentype::symbol;
				tmp += c;
			}
			else if (c == '"')
			{
				if (type == Tokentype::symbol)
					tokens.push_back(Token(type, tmp));
				else if (type != Tokentype::none)
					throw std::runtime_error("Invalid string token");
				type = Tokentype::string;
				state = State::string;
				tmp = "";
			}
			else if (c == ' ' || c == '\n' || c == '\r' || c == '\t')
			{
				if (type != Tokentype::none)
					tokens.push_back(Token(type, tmp));
				type = Tokentype::none;
				tmp = "";
			}
			else
			{
				std::stringstream ss;
				ss
					<< "Illegal token '"
					<< c
					<< "'";
				throw std::runtime_error(ss.str().c_str());
			}
		}
		else if (state == State::string)
		{
			if (c == '"')
			{
				state = State::normal;
			}
			else if (c == '\\')
			{
				state = State::stringescape;
			}
			else
			{
				tmp += c;
			}
		}
		else if (state == State::stringescape)
		{
			tmp += c;
			state = State::string;
		}
	}

	return tokens;
}
