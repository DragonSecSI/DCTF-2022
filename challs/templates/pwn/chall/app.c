#include <stdio.h>

int main()
{
	FILE *file;
	char flag[64];
	file = fopen("flag.txt", "r");
	fgets(flag, 63, file);
	printf("%s\n", flag);
	fclose(file);

	return 0;
}
