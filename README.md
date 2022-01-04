<p align="center">
  <img width="369" height="166" src=https://github.com/draumaz/savesys/blob/main/logo.png?raw>
</p>

A simple and clean, expandable, variable-based save system that's made to be easy to use.
Adapted from the save system used in my other project, [The Plains](https://github.com/draumaz/plains).

# How Does It Work?
Savesys uses an external text file for managing variables. It's easily called by a couple helpful commands that work silently to create the file your game needs.

# Commands

**save_generation()** is used to generate the save file. Save name and length are fully configurable.

**save_reader()** scans the file and returns numbers from the lines into an array. *You will need to adjust the array count to match your variables, please view the documentation appropriate for your language of choice for more information.*

**save_writer(line, num)** scans the line number and new number you pass into it, and writes to the file accordingly.

# Usage Instructions

You want to change the variable on line six to '7'.

*NOTE: line counts from zero; for line six, you will want to write '5'.*

## C++ Usage
```
#include "savesys.hpp"
save_writer(5, 7);
```
## Java Usage
```
savesys.write(5, 7);
```
## Python Usage
```
import savesys
savesys.saveWriter(5, 7)
```
