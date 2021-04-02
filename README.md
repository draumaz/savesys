# Savesys
A simple and clean, expandable, variable-based save system that's stupidly easy to use.
Adapted from the save system used in my other project, [The Plains](https://github.com/draumaz/plains).

# How Does It Work?
Savesys uses an external text file for managing variables. **saveGeneration** can generate this file. **saveReader** scans the file and assigns numbers from lines to variables, to be used however needed. **saveWriter** does the same thing, but for writing.

# How To Use
Example: Let's say on line 6, the current variable is 0, and we want to change this to 7.
NOTE: line_ext starts at zero, so for line six, five must be written.

import savesys

line_ext = 5

state_ext = 7

savesys.saveWriter(line_ext, state_ext)
