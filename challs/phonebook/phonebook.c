#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_PEOPLE 2


struct person {
	char phone_number[8];
	void (*call)(struct person *p);
	char *name;
	int name_length;
};

struct person *people[MAX_PEOPLE];


int main();
void business_call(struct person *p);
void friendly_call(struct person *p);
void love_call(struct person *p);
void menu();
void create(int person_id);
int get_index(int min, int max);
void print_menu();
int check(int value, int min, int max);
char *get_name();
void *choose_relation();
void print_relation_menu();
void edit(int person_id);
void print_edit_menu();
void edit_name(int person_id);
void edit_phone_number(int person_id);
void edit_relation(int person_id);


void business_call(struct person *p)
{
	long win;
	win = 0;
	win += 1;
	puts("------------------------------------------------------------");
	printf("Calling... %s\n", p->phone_number);
	printf("Hello %s", p->name);
	puts("I apologize for my absence on Friday. I wasn't feeling great");
	puts("------------------------------------------------------------");
}

void love_call(struct person *p)
{
	puts("------------------------------------------------------------");
	printf("Calling... %s\n", p->phone_number);
	printf("How you doin %s", p->name);
	puts("------------------------------------------------------------");
}

int main()
{
	menu();
	return 0;
}

void friendly_call(struct person *p)
{
	puts("------------------------------------------------------------");
	printf("Calling... %s\n", p->phone_number);
	printf("Hey %s", p->name);
	puts("Let's hang out!");
	puts("------------------------------------------------------------");
}

void menu()
{
	int cool[MAX_PEOPLE];
	for (int i = 0; i < MAX_PEOPLE; i++) cool[i] = 1;
	char *hidden_note = NULL;

	print_menu();
	int choice = get_index(1, 5);

	while (check(choice, 1, 5)) {
		if (choice == 1) {
			// create
			printf("Choose person id: ");
			int person_id = get_index(0, MAX_PEOPLE - 1);
			create(person_id);
		} else if (choice == 2) {
			// edit
			printf("Choose person id: ");
			int person_id = get_index(0, MAX_PEOPLE - 1);
			if (cool[person_id]) edit(person_id);
			else puts("Ahh nevermind...");
		} else if (choice == 3) {
			// print
			printf("Choose person id: ");
			int person_id = get_index(0, MAX_PEOPLE - 1);
			if (cool[person_id]) people[person_id]->call(people[person_id]);
			else puts("Ahh nevermind...");
		} else if (choice == 4) {
			// delete
			printf("Choose person id: ");
			int person_id = get_index(0, MAX_PEOPLE - 1);
			if (cool[person_id] && people[person_id] != NULL) {
				free(people[person_id]);
				free(people[person_id]->name);
				cool[person_id] = 0;
				printf("Person %d deleted!", person_id);
			}
			else  {
				puts("Ahh nevermind...");
			}
		}
		else {
			int size = 36;
			hidden_note = (char *)malloc(size + 1);
			printf("Hidden note: ");
			fgets(hidden_note, 2, stdin);
			fgets(hidden_note, size, stdin);
			hidden_note[size] = 0;
		}
		print_menu();
		choice = get_index(1, 5);
	}
	if (hidden_note != NULL) {
		free(hidden_note);
	}
	for (int i = 0; i < MAX_PEOPLE; i++) {
		if (people[i] != NULL) {
			free(people[i]->name);
			free(people[i]);
		}
	}
}

void edit(int person_id)
{
	if (people[person_id] == NULL) {
		puts("");
		printf("Person with person id %d doesn't exist", person_id);
		puts("");
	} else {
		print_edit_menu();
		int choice = get_index(1, 3);
		if (choice == 1) edit_name(person_id);
		else if (choice == 2) edit_phone_number(person_id);
		else edit_relation(person_id);
	}
}

void edit_relation(int person_id)
{
	people[person_id]->call = choose_relation();
}

void edit_phone_number(int person_id)
{
	printf("Enter new phone number: ");
	scanf("%8s", people[person_id]->phone_number);
}

void edit_name(int person_id)
{
	struct person *p = people[person_id];
	int length = p->name_length;
	printf("Name length: ");
	int size;
	scanf("%d", &size);
	// to fix shit
	fgets(p->name, 2, stdin);
	if (length != size) {
		free(p->name);
		p->name = (char *)malloc(size + 1);
	}
	printf("Name: ");
	fgets(p->name, size, stdin);
	(p->name)[size] = 0;
}

void print_edit_menu()
{
	puts("");
	puts("Choose an option: [1-3]");
	puts("1. Edit name");
	puts("2. Edit phone number");
	puts("3. Edit your relation");
	printf("> ");
}

// creates and stores a person to global array
void create(int person_id)
{
	if (people[person_id] == NULL) {
		struct person *p = (struct person *)malloc(sizeof(struct person));
		p->name = get_name();
		p->name_length = strlen(p->name);
		printf("Phone number: ");
		fgets(p->phone_number, 8, stdin);
		p->call = choose_relation();
		people[person_id] = p;
	} else {
		printf("Person with id %d already exists!", person_id);
	}
}

void *choose_relation()
{
	print_relation_menu();
	int choice = get_index(1, 3);
	if (choice == 1) return friendly_call;
	else if (choice == 2) return business_call;
	return love_call;
}

void print_relation_menu()
{
	puts("");
	puts("Select your relation: [1-3]");
	puts("1. Friends");
	puts("2. Business partners");
	puts("3. Lovers");
	printf("> ");
}

char *get_name()
{
	unsigned int size;
	printf("Name length: ");
	scanf("%u", &size);
	char *n = (char *)malloc(size + 1); // for nullbyte
	// to fix shit
	fgets(n, 2, stdin);
	printf("Name: ");
	fgets(n, size, stdin);
	n[size] = 0;
	return n;
}

int get_index(int min, int max)
{
	int index;
	scanf("%d", &index);
	while (!check(index, min, max)) {
		printf("Invalid choice! Try [%d-%d]\n", min, max);
		printf("> ");
		scanf("%d", &index);
	}
	return index;
}

void print_menu()
{
	puts("");
	puts("Choose an option: [1-5]");
	puts("1. Store someone's information");
	puts("2. Edit information");
	puts("3. Call someone");
	puts("4. Unfriend someone");
	puts("5. Add the hidden_note");
	printf("> ");
}

int check(int value, int min, int max)
{
	if (min <= value && value <= max)
		return 1;
	return 0;
}
