def saveWriter(line_ext, state_ext): #line_ext = line number from 0, state_ext = variable on line
    while True:
        try:
            file = open('data.txt', 'r') #opens the file for reading
            line = file.readlines() #collects line information
            line[line_ext] = state_ext #inputs state_ext on line_ext
            file = open('data.txt', 'w') #opens file for writing
            file.writelines(line) #writes to file
            file.close() #closes file
            return #returns to previous function
        except (FileNotFoundError, IndexError): #creates file if it doesn't exist
            file = open('data.txt', 'w') #opens file for writing
            file.write('0\n0\n0\n0\n0\n0\n0\n0\n0\n0') #writes ten zeros on ten lines
            file.close() #closes file
            Execute() #returns to beginning of controller script

def saveReader():
    file = open('data.txt', 'r') #opens file for reading
    line = file.readlines() #collects line information
    var1 = int(line[3]) #assigns line[3] to var1 as integer
    file.close() #closes file
    return var1 #returns to previous function with var1 status

def saveWriteReq():
    line_ext = 3 #sets line_ext (ex. line[3])
    state_ext = '7\n' #sets state_ext (ex. 7) NOTE must be in string form, affixed with \n
    saveWriter(line_ext, state_ext) #sends variables to script for processing
    return #returns to previous function

def Execute(): #order in which functions should be called
    saveWriteReq() #begin write process
    var1 = saveReader() #assign var1 to proper function
    print(var1) #optional: display variable
    quit()

Execute() #python script launch
