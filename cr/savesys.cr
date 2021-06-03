# Savesys, an easily-implementable save manager
# Written by draumaz in 2021
# BSD 3-Clause

def save_gen
        i = File.new "data.txt", "w" # Create file
        i.puts "0\n0\n0\n0\n0" # Write to file
        i.close
end

def save_write(line, state) # line - line number from 0; state - variable to insert
        write_in = save_read # Fetch current variables
        a = write_in[0] # Expand as necessary
        b = write_in[1]
        c = write_in[2]
        d = write_in[3]
        e = write_in[4]
        if line == 0 # Assign state to according variable
                a = state
        end
        if line == 1 # Expand as necessary
                b = state
        end
        if line == 2
                c = state
        end
        if line == 3
                d = state
        end
        if line == 4
                e = state
        end
        #if line == 5
                #f = state
        #end
        write_out = File.open "data.txt", "w" # Open file
        write_out.puts a,b,c,d,e # Write to file; expand as necessary
        write_out.close # Close file
end

def save_read
        x = File.read_lines "data.txt" # Open file for line read
        a = x[0].to_i # Assign lines to variable
        b = x[1].to_i # Expand as necessary
        c = x[2].to_i
        d = x[3].to_i
        e = x[4].to_i
        return [a,b,c,d,e] # Return as array
end
