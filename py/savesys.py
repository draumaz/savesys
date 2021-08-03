# Savesys, an easily-implementable save manager
# Written by draumaz in 2021
# BSD 3-Clause

import os

def config(pos):
    if pos == 0:
        return "default.txt" # This is what you want your save to be called...
    elif pos == 1:
        return 20 # ...and this is how many zeroes you want it to contain.

def exists():
    if (os.path.exists(config(0))): # If the file already exists, don't overwrite it...
        pass
    else: # ...otherwise, create and write to the file!
        open(config(0), "w+").write(config(1)*"0\n")

def read():
    return open(config(0), "r").readlines() # Return the entire file as an array of integers.

def write(line, state):
    i = read() # Retrieve the current states...
    i[line] = str(state) + "\n" # Replace the requested line with requested state...
    open(config(0), "w+").writelines(i) # ...and write it to the file!