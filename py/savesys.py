# Savesys, an easily-implementable save manager
# Written by draumaz in 2021
# BSD 3-Clause

def saveWriter(line_ext, state_ext): # line_ext = line number from 0, state_ext = variable on line
    state_write = str(state_ext) + '\n' # Converts state_ext to string and affixes '\n' to write without splash damage
    f = open('data.txt', 'r') # Opens the file for reading
    line = f.readlines() # Collects line information
    line[line_ext] = state_write # Inputs state variable on supplied line
    f = open('data.txt', 'w') # Opens file for writing
    f.writelines(line) # Writes to file
    f.close() # Closes file

def saveReader():
    file = open('data.txt', 'r') # Opens file for reading
    line = file.readlines() # Collects line information
    a = int(line[0]) # Assigns lines to variables, this should
    b = int(line[1]) # be infinitely configurable.
    c = int(line[2])
    d = int(line[3])
    e = int(line[4])
    #f = int(line[5])
    #g = int(line[6])
    #h = int(line[7])
    #and so on...
    file.close() # Closes file
    return [a, b, c, d, e] # Returns variables in an array, add to array if you have added more variables e.g. [a, b, c, d, e, f, g, h, coolvariable, epicvariable]

def saveGeneration(): # Save generator
    f = open('data.txt', 'w+') # Creates new file
    f.write('0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0') # Writes 15 zeroes (configurable, must match amount of variables in saveReader)
    f.close() # Closes the file
