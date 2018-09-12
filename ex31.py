print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input("> ")

# Checks if the user's input is the _string_ "1" (not the integer 1 which would require a conversion)
if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bar.")

    bear = input("> ")

    # These if, elif, else statements are inside the first block
    # They will only execute if the user's first response was "1"
    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

# If the first block didn't execute, checks if the user's input is "2"
elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    # This "if" statement is inside the second block and will only execute if the user's first response was "2"
    # It has two conditions and will execute if either of them are true
    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

# Catch-all if the user didn't input a "1" or "2"
else:
    print("You stumble around and fall on a knife and die. Good job!")