// Savesys, an easily-implementable save manage
// Written by draumaz in 2021
// BSD 3-Clause

#include <iostream>
#include <fstream>

void save_writer(int line, int state){ // line - line number from 0; state - variable to insert
	static int write_array[5]; // ADJUSTABLE: Create array
	std::ifstream write_in("data.txt"); // Open file for read
	write_in >> write_array[0] >> write_array[1] >> write_array[2] >> write_array[3] >> write_array[4]; // Assign lines to array
	write_array[line] = state; // Director
	std::ofstream write_out("data.txt"); // Open file for write
	write_out << write_array[0] << "\n" << write_array[1] << "\n" << write_array[2] << "\n" << write_array[3] << "\n" << write_array[4] << "\n"; // ADJUSTABLE: Write to file
}

int * save_reader(){
	static int read_array[4]; // ADJUSTABLE: Create array
	std::ifstream read_in("data.txt"); // Open file for reading
	read_in >> read_array[0] >> read_array[1] >> read_array[2] >> read_array[3] >> read_array[4]; // ADJUSTABLE: Assign to variables
	return read_array; // Return array
}

void save_generation(){
	std::ofstream gen("data.txt"); // ADJUSTABLE: Create file
	gen << "0\n0\n0\n0\n0\n"; // ADJUSTABLE: Write to file
}
