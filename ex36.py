# Corey Gray
# ex36.py - Designing and Debugging... An Adventure Game!
# A really simple text adventure using lists, functions, and modules (No objects!)

import ex36scenes # for scene descriptions

# Game Variables
weapons_and_armor = "covered in ice!"
coward = False

# Game Engine Functions
def game(): 
    ex36scenes.intro()
    input("Press any key to continue...")
    base()

def die():
    print("""You die.""")
    choice = input("Try again? ")
    if choice in ["yes", "y"]:
        game()
    else:
        exit()

# Scenes
def base():
    ex36scenes.base()
    while True:
        choice = input("What do you do? ")

        if choice == "look":
            ex36scenes.base()

        elif "look" in choice and "trail" in choice:
            print("""
Calling this narrow, winding path a 'trail' may be a bit generous, but there is a clear break in the snow-covered rocks
leading further up the mountain.
            """)

        elif "light" in choice and "fire" in choice:
            print("""
You light a fire in the sheltered alcove. Not only does your horse seem to appreciate it, but your weapons and armor
thaw out. Water slowly runs down the hard metal surfaces to coalesce in a pool around your feet, which is kind of
annoying, but you find it easier to move. Plus, you can actually draw your sword!
            """)
            global weapons_and_armor
            weapons_and_armor = "thawed!"
        
        elif ("go" in choice or "climb" in choice) and "trail" in choice:
            print("\nYou start climbing the trail higher up the mountain.")
            trail()

        elif choice == "quit":
            ex36scenes.quit()

        else:
            print("What was that? Try something else.")

def trail():
    ex36scenes.trail()
    while True:
        choice = input("What do you do? ")

        if choice == "look":
            ex36scenes.trail()
        
        elif choice in ["run", "flee", "retreat", "withdraw"]:
            print("\nYou turn tail and run back down the trail!")
            global coward
            coward = True
            base()
        
        elif ("draw" in choice and "sword" in choice) or choice in ["attack", "kill", "fight"]:
            global weapons_and_armor
            print("Your weapons and armor are",weapons_and_armor)
            if weapons_and_armor == "covered in ice!":
                print("""
You try to draw your sword and fight the minuscule goblins, but your sword is frozen to its scabbard. While you fumble
with the hilt, the goblins swarm over you and stab you repeatedly in the face.
                """)
                die()
            else:
                print("""
You slaughter those goblins. You slaughter them good.
                """)

        elif choice == "quit":
            ex36scenes.quit()

        else:
            print("What was that? Try something else.")

# Game Loop
game()