// Savesys, an easily-implementable save manager
// draumaz, 2021 | GPL v2

#include <iostream>
#include <fstream>

// begin config //
const int save_size = 5;
const char* save_name = "data.txt";
// end config //

int * save_reader() {
	static int array[save_size];
	std::ifstream read_in(save_name);
	for (int i = 0; i < save_size; i++) {
		read_in >> array[i]; // Loop read lines into array
	}
	return array;
}

void save_writer(int line, int state) {
	int * save_in = save_reader(); // Pull current values
	std::ofstream save_out(save_name);
	for (int i = 0; i < save_size; i++) {
		if (i == line) {
			save_out << state; // If loop is on supplied line, insert supplied state
		} else {
			save_out << save_in[i]; // Otherwise, reprint from save_in
		}
		save_out << "\n";
	}
}

void save_generation(){
	std::ofstream gen(save_name);
	for (int i = 0; i < save_size; i++) {
		gen << "0\n"; // Loop write five zeroes on new lines
	}
}

void save_exists() {
	std::ifstream i(save_name);
	if (i.fail()) {
		save_generation();
	}
}
