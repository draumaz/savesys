// Savesys, an easily-implementable save manage
// Written by draumaz in 2021
// BSD 3-Clause

#include <iostream>
#include <fstream>

int save_writer(int line, int state){ // line - line number from 0; state - variable to insert
	int a,b,c,d,e; // ADJUSTABLE: Generate variables
	std::ifstream write_in("data.txt"); // Open file for read
	write_in >> a >> b >> c >> d >> e; // Assign lines to variables
	if ( line == 0 ){ // ADJUSTABLE: Pointers
		a = state;
	}
	if ( line == 1 ){
		b = state;
	}
	if ( line == 2 ){
		c = state;
	}
	if ( line == 3 ){
		d = state;
	}
	if ( line == 4 ){
		e = state;
	}
	std::ofstream write_out("data.txt"); // Open file for write
	write_out << a << "\n" << b << "\n" << c << "\n" << d << "\n" << e << "\n"; // ADJUSTABLE: Write to file
	return 0;
}

int * save_reader(){
	int a,b,c,d,e; // ADJUSTABLE: Generate variables
	static int read_array[4]; // ADJUSTABLE: Create array
	std::ifstream read_in("data.txt"); // Open file for reading
	read_in >> a >> b >> c >> d >> e; // ADJUSTABLE: Assign to variables
	read_array[0] = a; // Assign array spaces as variables
	read_array[1] = b;
	read_array[2] = c;
	read_array[3] = d;
	read_array[4] = e;
	return read_array; // Return array
}

void save_generation(){
	std::ofstream gen("data.txt"); // ADJUSTABLE: Create file
	gen << "0\n0\n0\n0\n0\n"; // ADJUSTABLE: Write to file
}
