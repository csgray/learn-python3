# Creates a string of four format blocks and sets the value of the variable "formatter" to that string
formatter = "{} {} {} {}"

# Outputs the string with the blocks replaced by numbers
print(formatter.format(1, 2, 3, 4))
# Outputs the string with the blocks replaced by other strings
print(formatter.format("one", "two", "three", "four"))
# Outputs the string with the blocks replaced by Booleans
print(formatter.format(True, False, False, True))
# Outputs the string with the blocks replaced by more copies of "formatter" for sixteen blocks (4 * 4) total
print(formatter.format(formatter, formatter, formatter, formatter))
# Outputs the string with the blocks replaced by other strings which are entered on separate lines
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))