# Savesys
A simple and clean, expandable, variable-based save system that's made to be easy to use.
Adapted from the save system used in my other project, [The Plains](https://github.com/draumaz/plains).

# How Does It Work?
Savesys uses an external text file for managing variables. 

**saveGeneration**||**save_gen**||**generate** can be used to generate this file. By default, it names this file 'data.txt', but this is configurable.

**saveReader**||**save_read**||**read** scans the file and assigns numbers from lines to variables, to be used however needed. You will need to adjust the array count to match your variables, please view the documentation for more information.

**saveWriter**||**save_write**||**write** scans the line number and new variable you pass into it, and writes to the file accordingly.

# Usage Instructions

Let's say on you want to change the variable on line six to '7'.

NOTE: line counts from zero; for line six, you will want to write '5'.

## C++ Usage

#include "savesys.hpp"

int line = 5;

int state = 7;

save_writer(line, state);

## Crystal Usage

require "./savesys"

line = 5

state = 7

save_write(line, state)

## Python Usage

import savesys

line_ext = 5

state_ext = 7

savesys.saveWriter(line_ext, state_ext)

## Ruby Usage

require './savesys'

line_ext = 5

state_ext = 7

save_write(line_ext, state_ext)
