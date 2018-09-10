# Outputs a string
print("Mary had a little lamb.")
# Outputs a string with the placeholder {} filled by 'snow'
print("Its fleece was white as {}.".format('snow'))
# Outputs a string
print("And everywhere that Mary went.")
# Outputs "." ten times
print("." * 10) # what'd that do?

# These all set the value of a variable to a single-character string
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch end = ' ' at the end. try removing it to see what happens
# It replaces the default new-line at the end of the print function with a space
# These output a series of variables concatenated into one string
print(end1 + end2 + end3 + end4 + end5 + end6, end = ' ')
print(end7 + end8 + end9 + end10 + end11 + end12)