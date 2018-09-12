people = 30
cars = 40
trucks = 15


# The code indented below the 'if' statement will execute if the statement is true
if cars > people:
    # This will print if there are more cars than people
    print("We should take the cars.")
# If the 'if' statement isn't true, the 'elif' statement is checked and its code might be executed
elif cars < people:
    # This print if there are fewer cars than people
    print("We should not take the cars.")
# The code below the 'else' statement will execute if none of the previous statements are true
else:
    # This will print if the number of people and number of cars are equal
    print("We can't decide.")

if trucks > cars:
    # This will print if there are more trucks than cars
    print("That's too many trucks.")
elif trucks < cars:
    # This will print if there are fewer trucks than cars
    print("Maybe we could take the trucks.")
else:
    # This will print if the number of trucks and number of cars are equal
    print("We still can't decide.")

if people > trucks:
    # This will print if there are more people than trucks
    print("Alright, let's just take the trucks.")
else:
    # This will print if there are NOT more people than trucks
    print("Fine, let's stay home then.")