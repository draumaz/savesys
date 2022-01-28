#include <stdio.h>

#include "savesys.h"

int main() {
	save_exists(); // check existence, generate if not
	int * saves = save_reader(); // call array
	printf("Original line 2: %d", saves[1]);
	save_writer(1, 7); // write '7' to line 1
	saves = save_reader(); // recall
	printf("\nModified line 2: %d\n", saves[1]);
	return 0;
}
