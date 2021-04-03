# Savesys
A simple and clean, expandable, variable-based save system that's made to be easy to use.
Adapted from the save system used in my other project, [The Plains](https://github.com/draumaz/plains).

# How Does It Work?
Savesys uses an external text file for managing variables. 

**saveGeneration** can be used to generate this file. By default, it names this file 'data.txt', but this is configurable.

**saveReader** scans the file and assigns numbers from lines to variables, to be used however needed. 

**saveWriter** scans the line number and new variable you pass into it and writes to the file.

# How To Use
Example: Let's say on line 6, the current variable is 0, and we want to change this to 7.
NOTE: line_ext starts at zero, so for line six, five must be written.

import savesys

line_ext = 5

state_ext = 7

savesys.saveWriter(line_ext, state_ext)
