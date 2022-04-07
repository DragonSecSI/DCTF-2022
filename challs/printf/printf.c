#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main()
{
	alarm(30);
	char flag[32] = {0};
	FILE *file = fopen("flag.txt", "r");
	fgets(flag, 32, file);
	fclose(file);

	char input[21] = {0};

	// ask for name
	// what is your mother's name?
	puts("I'm going to Ljubljana tomorrow. What should I go take a look at?");
	fgets(input, 21, stdin);
	// no way, my mother's name is also %p
	// tell your name back
	printf("Wow, Ljubljana has ");
	printf(input);

	exit(0);
	return 0;
}
