# Savesys, an easily-implementable save manager
# Written by draumaz in 2021
# BSD 3-Clause

# Example script

import time
import sys
import savesys

savesys.saveGeneration() # Create save

variables = savesys.saveReader() # Call reader
var2 = variables[1] # Assign var2 to second variable from array

print("Your second variable is", var2, end="") 
print(".")

time.sleep(1)

line_ext = 1 # Assign line to 1
state_ext = 2 # Assign state to 2
savesys.saveWriter(line_ext, state_ext) # Call writer and pass variables

variables = savesys.saveReader()
var2 = variables[1]

print("...but now it's", var2, end="")
print('!')

time.sleep(2)

sys.exit()