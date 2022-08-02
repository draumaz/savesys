# Savesys

A simple, expandable, variable-based save system.

Forked from the save system used in my other project, [The Plains](https://github.com/draumaz/plains).

# Purpose

Savesys uses an external text file for managing variables. It's called by a couple commands that create files that you can later reference.

# Functions

- The ***generator*** is used to generate the save file. Save name and length are fully configurable.
- The ***existence checker*** checks to see if the file exists and generates one if not.
- The ***reader*** scans the file and returns numbers from the lines into an array. *You will need to adjust the array count to match your variables, view the documentation appropriate for your language of choice for more information.*
- The ***writer*** scans the line and new number you pass in, and writes to the file accordingly.

# Install

### C

#### Move "savesys.c" & "savesys.h" into your project.

### Rust

#### Add the following to your Cargo.toml file.
```
[dependencies]
savesys = "3.5.10"
```
