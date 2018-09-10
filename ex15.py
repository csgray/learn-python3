# Imports the argv module from the sys library
from sys import argv

# Sets the "script" and "filename" variables to the parameters passed when the script is launched
script, filename = argv

# Creates a file object and sets it as the value of the variable "txt" so that it can be manipulated
txt = open(filename)

# Prints explanatory text followed by the contents of the file
print(f"Here's your file {filename}:")
print(txt.read())

# Closes the file
txt.close()

# Prompts for another (or the same) file then sets the value of the "file_again" variable to that
print("Type the filename again:")
file_again = input("> ")

# Opens the second file and sets the value of the "txt_again" variable to that
txt_again = open(file_again)

# Outputs the contents of the second file
print(txt_again.read())

# Closes the second file
txt_again.close()