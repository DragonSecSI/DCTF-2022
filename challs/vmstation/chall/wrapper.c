#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>


void generate_name(char *str, size_t size)
{
	const char charset[] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJK...";
	int i = 5;
	while(i < size)
	{	
		str[i] = charset[(int) rand() % 25];
		++i;
	}
	str[size] = '\0';
}


int main()
{
	
	FILE * seed = fopen("/dev/random" ,"r");
	FILE * ptr;
	char randomdata[10];
	unsigned int seed_num;
	char ** args = (char **) malloc(40);
	int size = 0;
	

	fread(randomdata, 8,1,seed);
	seed_num = (unsigned int) *(int*)randomdata;
	fclose(seed);


	args[1] = (char *) malloc(100);
	args[0] = "vmstation4";
	srand(seed_num);

	strncpy(args[1],"/tmp/",5);

	generate_name(args[1], 80);

	ptr = fopen(args[1],"w"); 
	puts("Enter file size (in bytes): ");
	scanf("%d",&size);

	if (size >= 1000 ){
		puts("file size to big (max 1000)");
		return -1;
	}

	if (size <= 0 ){
		puts("file size needs to be positive integer!");
		return -1;
	}


	puts("Enter file contents: ");
	fgetc(stdin);
	for( int i = 0; i < size; ++i)
	{
		unsigned char c = fgetc(stdin);
		fputc(c,ptr);
	}


	//fgets(ptr,size,stdin);
	fclose(ptr);
//	int pid = fork();

//	if (pid == 0)
	execve("./vmstation",args,NULL);



	return 0;
}


