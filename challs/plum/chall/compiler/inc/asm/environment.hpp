#ifndef DCTF_ASM_ENVIRONMENT_HPP
#define DCTF_ASM_ENVIRONMENT_HPP

#include <vector>
#include <stack>
#include <string>
#include <utility>

namespace compiler
{
	class Environment
	{
		private:
			std::vector<std::string> strings;

			int depth = 0;
			int reg_counter = 0;
			uint8_t last_reg = -1;

		public:
			int add_string(std::string);
			std::vector<std::string> get_strings();

			int get_reg();
			void push_depth();
			void pop_depth();

			uint8_t get_last_reg();
			void set_last_reg(uint8_t reg);
	};
}

#endif
