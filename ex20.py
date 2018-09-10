from sys import argv

script, input_file = argv

# Prints all of a file's content
def print_all(f):
    print(f.read())

# Changes the file's position to the first byte
def rewind(f):
    f.seek(0)

# Reads a file's content until it encounters a new-line character then prints that content
def print_a_line(line_count, f):
    print(line_count, f.readline())

# Creates the file object from the script argument
current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)