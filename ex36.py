# Corey Gray
# ex36.py - Designing and Debugging... An Adventure Game!
# A really simple text adventure using lists, functions, and modules (No objects!)

import ex36scenes # for scene descriptions

# Game Variables
weapons_and_armor = "covered in ice!"
coward = False
grappling_hook = False

# Game Engine Functions
def game(): 
    ex36scenes.intro()
    input("Press any key to continue...")
    base()

def die():
    print("You die. And with you dies all hope of restoring cosmic balance to the lands of Fife.")
    choice = input("To be the chosen one, a hero must rise to the test. Will you try again? ")
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
            trail1()

        elif choice == "quit":
            ex36scenes.quit()

        else:
            print("What was that? Try something else.")

def trail1():
    ex36scenes.trail1()
    while True:
        choice = input("What do you do? ")

        if choice == "look":
            ex36scenes.trail1()
        
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
You draw your sword from its weatherworn sheath and an epic battle is fight! The creatures are as weak as they are evil
and they swing their oversized blades in wide, slow arcs, but for every goblin that you cut down it seems two more
spring from some hole in the snow to join the fray. Soon their black blood covers the snow, which has been churned into
a thick slush beneath your boots, and the sound of steel on steel echos through the mountains.

The battle ends with the last goblin's head rolling off of its shoulders and falling at your feet.
                """)
                trail2()

        elif choice == "quit":
            ex36scenes.quit()

        else:
            print("What was that? Try something else.")

def trail2():
    ex36scenes.trail2()
    while True:
        choice = input("What do you do? ")

        if choice == "look":
            ex36scenes.trail2()

        elif ("look" in choice or "search" in choice) and ("goblins" in choice or "corpse" in choice):
            print("""
Gross. The only thing that smells worse than a goblin's outsides is a goblin's insides, and thanks to your handy skill
at epic fights, there's a bunch of goblin insides now outside and steaming. You pick over the battlefield with a
practiced eye but don't find anything worth taking.""")

        elif ("look" in choice or "search" in choice) and "holes" in choice:
            print("""
There are multiple holes at the base of the trees surrounding the clearing which lead to a maze of tunnels which are
too short to move through. That and they smell like something died. Many somethings died. Most of the holes are filled
with worthless trash, but in one of them you find an adventurer's pack containing a grappling hook.
            """)
            global grappling_hook
            grappling_hook = True

        elif ("go" in choice or "climb" in choice) and "trail" in choice:
            print("\nYou continue up the trail higher into the mountains.")
            cliff()

        elif choice == "quit":
            ex36scenes.quit()

        else:
            print("What was that? Try something else.")

def cliff():
    ex36scenes.cliff()
    while True:
        choice = input("What do you do? ")
        
        if choice == "look":
            ex36scenes.trail2()

        elif choice == "quit":
            ex36scenes.quit()

        else:
            print("What was that? Try something else.")

# Game Loop
game()