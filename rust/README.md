# Savesys

A simple, expandable, variable-based save system.

Forked from the save system used in my other project, [The Plains](https://git.goatopossum.com/draumaz/plains).

# Functions

- ```generate(SAVE_NAME: &'static str, num: i32)``` is self-explanatory.
- ```exists(SAVE_NAME: &'static str)``` checks to see if the SAVE_NAME exists and returns the corresponding boolean.
- ```reader(SAVE_NAME: &'static str)``` scans SAVE_NAME and returns the numbers from the file into a Vec<i32>.
- ```writer(SAVE_NAME: &'static str, line: usize, state: i32)``` scans the line and new number passed in, and writes to SAVE_NAME.

## Example Usage

```
extern crate savesys;
use savesys::*;

if ! exists("data.txt") { generate("data.txt", 20) };

let save_vec: Vec<i32> = savesys::reader("data.txt");
if ! save_vec[5] == 7 { writer("data.txt", 5, 7) }
```
