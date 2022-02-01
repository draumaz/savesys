// Savesys, an easily-implementable save manager
// draumaz, 2022 | GPL v3

#include <stdio.h>
#include <unistd.h>

// begin config
#define save_length 12
const char* save_name = "data.txt";
// end config

int * save_reader() {
	static int array[12];
	int i = 0;
	int x = 0;
	FILE *read_in = fopen(save_name, "r");
	fscanf(read_in, "%d", &i);
	while (!feof (read_in)) {
		array[x] = i; x += 1;
		fscanf(read_in, "%d", &i);
	} return array;
}

void save_writer(int line, int state) {
	if (state < 0) { state = 0; }
	int * save_in = save_reader();
	FILE *read_out = fopen(save_name, "w");
	for (int i = 0; i < save_length; i++) {
		if (i == line) {
			fprintf(read_out, "%d\n", state);
		} else {
			fprintf(read_out, "%d\n", save_in[i]);
		}
	} fclose(read_out);
}

void save_generate() {
	FILE *generate = fopen(save_name, "w");
	for (int i = 0; i < save_length; i++) {
		fprintf(generate, "%d\n", 0);
	} fclose(generate);
}

void save_exists() {
	if (access(save_name,F_OK) == -1) {
		save_generate();
	}
}
