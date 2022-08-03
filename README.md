# Savesys

A simple, expandable, variable-based save system.

Forked from the save system used in my other project, [The Plains](https://git.goatopossum.com/draumaz/plains).

# Functions

- ```generate()``` is self-explanatory.
- ```exists()``` checks to see if the save file exists and returns the corresponding boolean.
- ```reader()``` scans the file and returns the numbers from the file into a Vec<i32>.
- ```writer()``` scans the line and new number passed in, and writes to SAVE_NAME.

# Install

### C

#### Move "savesys.c" & "savesys.h" into your project.

### Rust

#### Add the following to your Cargo.toml file.
```
[dependencies]
savesys = "3.5.11"
```
