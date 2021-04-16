# Savesys, an easily-implementable save manager
# Written by draumaz in 2021
# BSD 3-Clause

def saveWriter(line_ext, state_ext): #line_ext = line number from 0, state_ext = variable on line
    state_write = str(state_ext) + '\n' #converts state_ext to string and affixes '\n' to write without splash damage
    f = open('data.txt', 'r') #opens the file for reading
    line = f.readlines() #collects line information
    line[line_ext] = state_write #inputs state variable on supplied line
    f = open('data.txt', 'w') #opens file for writing
    f.writelines(line) #writes to file
    f.close() #closes file

def saveReader():
    file = open('data.txt', 'r') #opens file for reading
    line = file.readlines() #collects line information
    a = int(line[0]) #assigns lines to variables, this should
    b = int(line[1]) #be infinitely configurable.
    c = int(line[2])
    d = int(line[3])
    e = int(line[4])
    #f = int(line[5])
    #g = int(line[6])
    #h = int(line[7])
    #and so on...
    file.close() #closes file
    return [a, b, c, d, e] #returns variables in an array, add to array if you have added more variables e.g. [a, b, c, d, e, f, g, h, coolvariable, epicvariable]

def saveGeneration(): #Save generator
    f = open('data.txt', 'w+') #creates new file
    f.write('0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0') #writes 15 zeroes (configurable, must match amount of variables in saveReader)
    f.close() #closes the file
