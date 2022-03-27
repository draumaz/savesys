<p align="center">
  <img width="369" height="166" src=https://github.com/draumaz/savesys/blob/main/logo.png?raw>
</p>

A simple, expandable, variable-based save system.

Forked from the save system used in my other project, [The Plains](https://github.com/draumaz/plains).

# Purpose

Savesys uses an external text file for managing variables. It's called by a couple commands that create files that you can later reference.

# Functions

- The generator is used to generate the save file. Save name and length are fully configurable.
- The existence checker checks to see if the file exists and generates one if not.
- The reader scans the file and returns numbers from the lines into an array. *You will need to adjust the array count to match your variables, view the documentation appropriate for your language of choice for more information.*
- The writer scans the line and new number you pass in, and writes to the file accordingly.

# Install

#### First - clone the repo, and find the folder pertaining to the language you're going to use.

### C

#### Move "savesys.c" & "savesys.h" into your project.

### C++

#### Move "savesys.cpp" & "savesys.hpp" into your project.

### Python

#### Move "savesys.py" into your project.

### Rust

#### Add the following line to your Cargo.toml file.
```
[dependencies]
savesys = "3.5.0"
```
### Shell

#### Move "savesys.sh" into your project.

# Usage Example

You want to change the variable on line six to '7'.

*NOTE: line counts from zero; for line six, you will want to write the numeral 5.*

## C

```
#include "savesys.h"
save_writer(5, 7);
```

## C++

```
#include "savesys.hpp"
save_writer(5, 7);
```

## Python

```
import savesys
savesys.writer(5, 7)
```

## Rust

```
use savesys;
savesys::writer(5, 7)
```

## Shell

```
source ./savesys.sh
save_writer 5 7
```
