# Savesys

A simple, expandable, variable-based save system.

## IMPORTANT MESSAGE FOR C PORT:
## Open savesys.c and change the config macros
## to what you'd like them to be.

Forked from the save system used in my other project, [The Plains](https://github.com/draumaz/plains).

# Purpose

Savesys uses an external text file for managing variables. It's called by a couple commands that create files that you can later reference.

# Functions

- ```save_generate()``` is used to generate the save file.
- ```save_exists()``` checks to see if the file exists and returns a corresponding boolean.
- ```save_reader()``` scans SAVE_NAME and returns the numbers from the file into a Vec<i32>.
- ```save_writer(line, num)``` scans the line and new number you pass in, and writes to the file.

## Example Usage

```
#include "savesys.h"

save_exists();
int * saves = save_reader();
printf("Original line 2: %d", saves[1]);
save_writer(1, 7); // write '7' to line 1
saves = save_reader();
printf("\nModified line 2: %d\n", saves[1]);
return 0;
```
