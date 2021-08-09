# Savesys, an easily-implementable save manager
# Written by draumaz in 2021
# BSD 3-Clause

import os

def config(pos):
    if pos == 0:
        return "default.txt" # This is what you want your save to be called...
    elif pos == 1:
        return 20 # ...and this is how many zeroes you want it to contain. (this starts from 0!)

def exists():
    if (os.path.exists(config(0))): # If the file already exists, don't overwrite it...
        pass
    else: # ...otherwise, create and write to the file!
        open(config(0), "w+").write(config(1)*"0\n")

def read():
    return list(map(int, open(config(0), "r").readlines())) # Return the entire file as an array of integers.

def write(line, state):
    i = read() # Retrieve the current states...
    f = open(config(0), "w") # ...open the file...
    for x in range (0, config(1)): # ...set ranges....
        if x == line:
            f.write(str(state) + "\n") # ...and write the states...
            continue
        f.write(str(i[x]) + "\n") # ...to the file!
