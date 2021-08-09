# Savesys
A simple and clean, expandable, variable-based save system that's made to be easy to use.
Adapted from the save system used in my other project, [The Plains](https://github.com/draumaz/plains).

# How Does It Work?
Savesys uses an external text file for managing variables. It's easily called by a couple helpful commands that work silently to create the file your game needs.

# Commands

**saveGeneration**||**save_gen**||**generate** is used to generate the save file. Save name and length are fully configurable inside of Savesys.

**saveReader**||**save_read**||**read** scans the file and assigns numbers from lines to variables, to be used however needed. *You will need to adjust the array count to match your variables, please view the documentation appropriate for your language of choice for more information.*

**saveWriter**||**save_write**||**write** scans the line number and new number you pass into it, and writes to the file accordingly.

# Usage Instructions

Let's say on you want to change the variable on line six to '7'.

*NOTE: line counts from zero; for line six, you will want to write '5'.*

## C# Usage
```
using Savesys;
Savesys sav = new();
sav.write(5,7);
```
## C++ Usage
```
#include "savesys.hpp"
save_writer(5, 7);
```
## Crystal Usage
```
require "./savesys"
save_write(5, 7)
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
## Ruby Usage
```
require './savesys'
save_write(5, 7)
```
