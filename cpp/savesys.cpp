// Savesys, an easily-implementable save manage
// Written by draumaz in 2021
// BSD 3-Clause

#include <iostream>
#include <fstream>

void save_writer(int line, int state){ // line - line number from 0; state - variable to insert
	static int v[5]; // ADJUSTABLE: Create array
	std::ifstream write_in("data.txt"); // Open file for read
	write_in >> v[0] >> v[1] >> v[2] >> v[3] >> v[4]; // Assign lines to array
	v[line] = state; // Director
	std::ofstream write_out("data.txt"); // Open file for write
	write_out << v[0] << "\n" << v[1] << "\n" << v[2] << "\n" << v[3] << "\n" << v[4] << "\n"; // ADJUSTABLE: Write to file
}

int * save_reader(){
	int a,b,c,d,e; // ADJUSTABLE: Generate variables
	static int read_array[4]; // ADJUSTABLE: Create array
	std::ifstream read_in("data.txt"); // Open file for reading
	read_in >> read_array[0] >> read_array[1] >> read_array[2] >> read_array[3] >> read_array[4]; // ADJUSTABLE: Assign to variables
	return read_array; // Return array
}

void save_generation(){
	std::ofstream gen("data.txt"); // ADJUSTABLE: Create file
	gen << "0\n0\n0\n0\n0\n"; // ADJUSTABLE: Write to file
}
