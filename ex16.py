from sys import argv

# Retrieves the command-line arguments and sets the values of variables to them.
# The first argument of argv is always the scriptname.
script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w') # The 'w' opens filename in 'write' mode instead of the default 'read' mode

print("Truncating the file. Goodbye!")
target.truncate() # We don't actually need this when opening a file in 'write' mode since Python truncates it first.

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

# Makes a string of each line followed by a new-line and outputs it to the file.
target.write(f"{line1}\n{line2}\n{line3}\n")

# Closes the file when we're done, which is good housekeeping
print("And finally, we close it.")
target.close()