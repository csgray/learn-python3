# Sets the value of "types of people" to 10
types_of_people = 10
# Creates an f-string formatted with the value of "types_of_people" then sets "x" to it
x = f"There are {types_of_people} types of people."

# Sets the value of "binary" to the string "binary"
binary = "binary"
# Sets the value of "do_not" to the string "don't"
do_not = "don't"
# Creates an f-string formatted with the values of "binary" and "do_not" then sets "y" to it
y = f"Those who know {binary} and those who {do_not}."

# Outputs the value of "x"
print(x)
# Outputs the value of "y"
print(y)

# Outputs an f-string formatted with the value of "x"
print(f"I said: {x}")
# Outputs an f-string formatted with the value of "y"
print(f"I also said: '{y}'")

# Sets the value of "hilarious" to False
hilarious = False
# Sets the value of "joke_evaluation" to a string with a placeholder for a variable
joke_evaluation = "Isn't that joke so funny?! {}"

# Outputs the value of "joke_evaluation" with the placeholder set to the value of "hilarious"
print(joke_evaluation.format(hilarious))

# Creates a string and sets the value of "w" to it
w = "This is the left side of..."
# Creates a string and sets the value of "e" to it
e = "a string with a right side."

# Concatenates the values of "w" and "e" then outputs the result
print(w + e)