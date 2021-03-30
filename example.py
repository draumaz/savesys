###SAVESYS, A STUPIDLY EASY SAVE SYSTEM###
###WRITTEN BY DRAUMAZ###
###LICENSE: BSD 3-CLAUSE###

###EXAMPLE SCRIPT###

import time
import sys
import os
import savesys

savesys.saveGeneration() #Create save

variables = savesys.saveReader() #Call reader
var2 = variables[1] #assign var2 to line 1

print("Your second variable is", var2, end="") 
print(".")

time.sleep(2)

line_ext = 1 #assign line 1 for writing
state_ext = 2 #change state to 2
savesys.saveWriter(line_ext, state_ext) #Call writer

variables = savesys.saveReader()
var2 = variables[1]

print("...but now it's", var2, end="")
print('!')

time.sleep(2)

sys.exit()