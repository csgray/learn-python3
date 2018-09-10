# Here's some new strange stuff, remember type it exactly.

# Creates a string and sets the value of "days" to that string
days = "Mon Tue Wed Thu Fri Sat Sun"
# Creates a string and sets the value of "months" to that string
# \n is the escaped character for a new line so that each month is on its own line
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

# Outputs a string with the value of "days" concatenated to the end
print("Here are the days: ", days)
# Outputs a string with the value of "months" concatenated to the end, new lines and all
print("Here are the months: ", months)

# Outputs a multi-line string
print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")