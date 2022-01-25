<p align="center">
  <img width="369" height="166" src=https://github.com/draumaz/savesys/blob/main/logo.png?raw>
</p>

A simple, expandable, variable-based save system.

Forked from the save system used in my other project, [The Plains](https://github.com/draumaz/plains).

# Function

Savesys uses an external text file for managing variables. It's called by a couple commands that create files that you can later reference.

# Commands

**save_generation()** | **savesys.gen()** is used to generate the save file. Save name and length are fully configurable.

**save_exists()** | **savesys.exists()** checks to see if the file exists and generates one if not.

**save_reader()** | **savesys.reader()** scans the file and returns numbers from the lines into an array. *You will need to adjust the array count to match your variables, view the documentation appropriate for your language of choice for more information.*

**save_writer(line, num)** | **savesys.writer(line, num)** scans the line and new number you pass in, and writes to the file accordingly.

# Usage Example

You want to change the variable on line six to '7'.

*NOTE: line counts from zero; for line six, you will want to write the numeral 5.*

## C++ Usage
```
#include "savesys.hpp"
save_writer(5, 7);
```
## Python Usage
```
import savesys
savesys.writer(5, 7)
```
## Bash Usage
```
source ./savesys.sh
save_writer 5 7
```
