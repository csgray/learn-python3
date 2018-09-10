# imports the argv function, which takes input from the command line when the script is called, from the sys module
from sys import argv
# unpacks argv and assigns its content to the following variables in order from left to right
script, first, second, third = argv

# Output with each of the unpacked variables
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)