# Savesys, an easily-implementable save manager
# Written by draumaz in 2021
# BSD 3-Clause

def save_gen
  file = File.open('data.txt', 'w') # Create file
  File.write('data.txt', "0\n0\n0\n0\n0") # Write to file
  return
end

def save_write(line_ext, state_ext) # line_ext - line number from 0; state_ext - variable to insert
  save = File.open('data.txt', 'r+') do |file| # Open file
    lines = file.each_line.to_a # Retrieve line information
    lines[line_ext] = state_ext, "\n" # Assign
    file.rewind # Ruby magic
    file.write(lines.join) # Write to file
    return
  end
end

def save_read
  save = File.open('data.txt', 'r') # Open file
  var1 = Integer(save.readlines[0]) # Assign line to variable
  save = File.open('data.txt', 'r') # Expandable
  var2 = Integer(save.readlines[1])
  save = File.open('data.txt', 'r')
  var3 = Integer(save.readlines[2])
  save = File.open('data.txt', 'r')
  var4 = Integer(save.readlines[3])
  save = File.open('data.txt', 'r')
  var5 = Integer(save.readlines[4])
  save.close # Close file
  return var1, var2, var3, var4, var5 # Return array
end
