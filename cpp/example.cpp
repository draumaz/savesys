#include <iostream>
#include "savesys.hpp"

int main(){
        
        save_generation(); // Generate save file

        int * variables = save_reader(); // Assign reader array to int
        int var2 = variables[1]; // Assign var2 to second item in array

        std::cout << "var2 (line 1) was " << var2 << "." << std::endl;

        int line = 1; // Assign line to '1' (line 2)
        int state = 2; // Assign state to '2'
        save_writer(line, state); // Write
        
        int * variables_2 = save_reader();
        int var2_new = variables_2[1];

        std::cout << "It has been changed to " << var2_new << "." << std::endl;

        exit(0);

}
