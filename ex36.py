# Corey Gray
# ex36.py - Designing and Debugging... An Adventure Game!
# This cries out for objects, but I'm going to use the tools provided: print statements, functions, and branching

# Game Variables
inventory = []
score = 0

# Rooms
def gate():
    print("This is a gate!")

def courtyard():
    print("This is a courtyard!")

def hall():
    print("This is the main hall!")

def throne():
    print("This is the throne room!")

def west_tower():
    print("This is the western tower!")

def princess():
    print("This is the princess's room!")

def east_tower():
    print("This is the eastern tower!")

def wizard():
    print("This is the wizard's room!")

def dungeon():
    print("This is the dungeon!")

def dragon():
    print("This is the dragon's lair!")

def start():
    print("This is a game!")

# Functions
def inventory():
    print ("You have the following items: ")
    for item in inventory:
        print(item)

def score():
    print ("Your current score is: ", score)

# Game
start()