# Savesys
A simple and clean, expandable, variable-based save system that's made to be easy to use.
Adapted from the save system used in my other project, [The Plains](https://github.com/draumaz/plains).

# How Does It Work?
Savesys uses an external text file for managing variables. 

**saveGeneration** can be used to generate this file. By default, it names this file 'data.txt', but this is configurable.

**saveReader** scans the file and assigns numbers from lines to variables, to be used however needed. You will need to adjust the array count to match your variables, please view the documentation for more information.

**saveWriter** scans the line number and new variable you pass into it, and writes to the file accordingly.

# How To Use
Let's say on you want to change the variable on line six to '7'.

NOTE: line_ext counts from zero; for line six, you will want to write '5'.

import savesys

line_ext = 5

state_ext = 7

savesys.saveWriter(line_ext, state_ext)
