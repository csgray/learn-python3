# Corey Gray
# ex36.py - Designing and Debugging... An Adventure Game!
# This cries out for objects, but I'm going to use the tools provided: print statements, functions, and branching


# Variables
prompt = "What do you do? "

# Rooms
def gate():
    print("\nThis is a gate!")
    choice = input(prompt)
    if "north" in choice:
        courtyard()
    else:
        print("That doesn't work.")
        gate()

def courtyard():
    print("This is a courtyard!")
    choice = input(prompt)
    if "north" in choice:
        hall()
    elif "south" in choice:
        gate()
    else:
        print("That doesn't work.")
        courtyard()

def hall():
    print("This is the main hall!")
    choice = input(prompt)
    if "up" in choice or "stair" in choice:
        throne()
    elif "west" in choice:
        west_tower()
    elif "east" in choice:
        east_tower()
    elif "down" in choice:
        dungeon()
    elif "south" in choice:
        courtyard()
    else:
        print("That doesn't work.")
        hall()

def throne():
    print("This is the throne room!")
    choice = input(prompt)
    if "down" in choice or "stair" in choice:
        hall()
    else:
        print("That doesn't work.")
        throne()

def west_tower():
    print("This is the western tower!")
    choice = input(prompt)
    if "up" in choice or "stair" in choice:
        princess()
    elif "east" in choice:
        hall()
    else:
        print("That doesn't work.")
        west_tower()

def princess():
    print("This is the princess's room!")
    choice = input(prompt)
    if "down" in choice or "stair" in choice:
        west_tower()
    else:
        print("That doesn't work.")
        princess()

def east_tower():
    print("This is the eastern tower!")
    choice = input(prompt)
    if "up" in choice or "stair" in choice:
        wizard()
    elif "west" in choice:
        hall()
    else:
        print("That doesn't work.")
        east_tower()

def wizard():
    print("This is the wizard's room!")
    choice = input(prompt)
    if "down" in choice or "stair" in choice:
        east_tower()
    else:
        print("That doesn't work.")
        wizard()

def dungeon():
    print("This is the dungeon!")
    choice = input(prompt)
    if "up" in choice:
        hall()
    if "south" in choice:
        dragon()
    else:
        print("That doesn't work.")
        dungeon()

def dragon():
    print("This is the dragon's lair!")
    choice = input(prompt)
    if "north" in choice:
        dungeon()
    else:
        print("That doesn't work.")
        dragon()

def start():
    print("One thousand years ago, this ancient citadel fell to an evil wizard. His evil infected the land causing crops to fail, the dead to rise, and the peasants to flee. Many heroes have challenged the wizard and failed. Can you succeed?")
    gate()


# Game
start()