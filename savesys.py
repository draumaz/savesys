def saveWriter(line_ext, state_ext): #line_ext = line number from 0, state_ext = variable on line
    file = open('data.txt', 'r') #opens the file for reading
    line = file.readlines() #collects line information
    line[line_ext] = state_ext #inputs state_ext on line_ext
    file = open('data.txt', 'w') #opens file for writing
    file.writelines(line) #writes to file
    file.close() #closes file
    return #returns to previous function

def saveReader():
    file = open('data.txt', 'r') #opens file for reading
    line = file.readlines() #collects line information
    var1 = int(line[3]) #assigns line[3] to var1 as integer
    file.close() #closes file
    return var1 #returns to previous function with var1 status

def saveWriteReq(): #template, use this function in other scripts and call back
    line_ext = 3 #sets line_ext (ex. line[3])
    state_ext = '7\n' #sets state_ext (ex. 7) NOTE must be in string form, affixed with \n
    saveWriter(line_ext, state_ext) #sends variables to script for processing
    return #returns to previous function

#USAGE:
#saveWriteReq() start write process
#var1 = saveReader() assign variable from read function
