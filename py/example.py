# Savesys, an easily-implementable save manager
# Written by draumaz in 2021
# BSD 3-Clause

# Example script

import time
import sys
import savesys

savesys.exists() # Generate/check file

print("Your second variable is", savesys.read()[1], end="")
print(".")

time.sleep(1)

savesys.write(1, 7) # Write variable 7 to line 1

print("...but now it's", savesys.read()[1], end="")
print('!')

time.sleep(2)

sys.exit()
