# Savesys

A simple, expandable, variable-based save system.

Forked from the save system used in my other project, [The Plains](https://github.com/draumaz/plains).

# Purpose

Savesys uses an external text file for managing variables. It's called by a couple commands that create files that you can later reference.

# Functions

- ```generate(SAVE_NAME: &'static str, num: i32)``` is used to generate the save file.
- ```exists(SAVE_NAME: &'static str)``` checks to see if the file exists and returns a corresponding boolean.
- ```reader(SAVE_NAME: &'static str)``` scans SAVE_NAME and returns the numbers from the file into a Vec<i32>.
- ```writer(SAVE_NAME: &'static str, line: usize, state: i32)``` scans the line and new number you pass in, and writes to the file.

## Example Usage

```
extern crate savesys;
use savesys::*;

if exists("data.txt") == false { generate("data.txt", 20) };

writer("data.txt", 5, 7);

let save_vec: Vec<i32> = savesys::reader("data.txt");
```
