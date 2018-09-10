from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# Opens a file and reads its contents to the 'indata' variable
indata = open(from_file).read()

# len() returns the number of items (bytes) in a container (string)
print(f"The input file is {len(indata)} bytes long")
# exists() checks if a file, based on the string argument, already exists and returns True/False as appropriate
print(f"Does the output file exist? {exists(to_file)}")

# Opens a file in 'write' mode then writes the value of 'indata' to it
open(to_file, 'w').write(indata)

print("Alright, all done.")