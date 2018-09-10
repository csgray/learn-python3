print("Let's practice everything.")
# This is a single-quote string so we need to escape the apostrophes inside the string
print('You\'d need to know \'bout escapes with \\ that do:')
# Basic formatting with new-lines and tabs
print('\n newlines and \t tabs.')

# Multi-line string with new-lines and tabs
poem ="""
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------")
print(poem)
print("--------------")

# Simple arithmetic and declaring a variable
five = 10 - 2 + 3 - 6
# f-string for formatting by inserting a variable into a string
print(f"This should be five: {five}")

# Function definition
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    # Returns three values
    return jelly_beans, jars, crates


start_point = 10000
# Creates three separate variables and sets them to the values returned by secret_formula in order
beans, jars, crates = secret_formula(start_point)

# Formats the string by calling .format() on it
print("With a starting point of: {}".format(start_point))
# Another f-string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

# Updates the value of start_point to the old value divided by 10
start_point = start_point / 10

print("We can also do that this way:")
# Declares a variable with multiple values
formula = secret_formula(start_point)
# Calls .format() and passes to it the multiple values of formula which are inserted in order 
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))