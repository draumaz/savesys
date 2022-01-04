# Savesys, an easily-implementable save manager
# Written by draumaz in 2021
# BSD 3-Clause

import os

## begin config ##
save_name = "default.txt"
save_size = 20
save_contents = "0"
## end config ##

def exists():
    if not (os.path.exists(save_name)): # If the file doesn't exist...
        open(save_name, "w+").write(save_size*(save_contents+"\n")) # ...create it, and fill it using config values.

def read():
    return list(map(int, open(save_name, "r").readlines())) # Return the entire file as an array of integers.

def write(line, state):
    arr = read() # Retrieve the current states...
    f = open(save_name, "w") # ...open the file...
    for i in range(0, save_size): # ...set loop ranges....
        if i == line:
            f.write(str(state)+"\n") # ...if the loop matches line, write state...
            continue
        f.write(str(arr[i])+"\n") # ...and write to the file!
