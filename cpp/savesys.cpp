// Savesys, an easily-implementable save manage
// Written by draumaz in 2021
// BSD 3-Clause

#include <iostream>
#include <fstream>

const char* string_paths(int pnt) {
	const char* path = NULL;
	switch (pnt) {
		case 0:
			path = "data.txt"; // Adjustable file name
			break;
	}
	return path;
}

int * save_reader() {
	static int array[5]; // Adjust number
	std::ifstream read_in(string_paths(0));
	for (int i = 0; i < 5; i++) { // Adjust number
		read_in >> array[i]; // Loop read lines into array
	}
	return array;
}

void save_writer(int line, int state) {
	int * save_in = save_reader(); // Pull current values
	std::ofstream save_out(string_paths(0));
	for (int i = 0; i < 5; i++) { // Adjust number
		if (i == line) {
			save_out << state; // If loop is on supplied line, insert supplied state
		} else {
			save_out << save_in[i]; // Otherwise, reprint from save_in
		}
		save_out << "\n";
	}
}

void save_generation(){
	std::ofstream gen(string_paths(0)) ;
	for (int i = 0; i < 5; i++) { // Adjust number
		gen << "0\n"; // Loop write five zeroes on new lines
	}
}
