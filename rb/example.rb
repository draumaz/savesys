# Savesys, an easily-implementable save manager
# Written by draumaz in 2021
# BSD 3-Clause

# Example script

require './savesys'

save_gen() # Generate save

var2 = save_read[1] # Assign var2 to second item in array

puts var2

line_ext = 1 # Assign line to '1' (line 2)
state_ext = 2 # Assign state to '2'
save_write(line_ext, state_ext) # Write

var2 = save_read[1] # Assign again

puts var2
