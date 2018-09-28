# Corey Gray
# ex36.py - Designing and Debugging... An Adventure Game!
# A really simple text adventure using lists, functions, and modules (No objects!)

import ex36strings # for scene descriptions


# Game Variables
weapons_and_armor = "covered in ice!"
coward = False
grappling_hook = False
on_rocks = False


# Game Engine Functions
def game(): 
    ex36strings.intro()
    input("Press any key to continue...")
    base()

def quit():
    ex36strings.quit()
    exit()


def die():
    print("You die. And with you dies all hope of restoring cosmic balance to the lands of Dundee.")
    choice = input("To be the chosen one, a hero must rise to the test. Will you try again? ")
    if choice in ["yes", "y"]:
        # Reset Game Variables
        global weapons_and_armor
        weapons_and_armor = "covered in ice!"
        global coward
        coward = False
        global grappling_hook
        grappling_hook = False
        global on_rocks
        on_rocks = False

        # Restart game
        game()

    else:
        exit()


# Scenes
def base():
    ex36strings.base()
    while True:
        choice = input("What do you do? ")

        if choice == "look":
            ex36strings.base()

        elif "look" in choice and "trail" in choice:
            ex36strings.look_trail()

        elif "light" in choice and "fire" in choice:
            ex36strings.light_fire()
            global weapons_and_armor
            weapons_and_armor = "thawed!"
        
        elif ("go" in choice or "climb" in choice) and "trail" in choice:
            print("\nYou start climbing the trail higher up the mountain.")
            trail1()

        elif choice == "quit":
            quit()

        else:
            print("What was that? Try something else.")


def trail1():
    ex36strings.trail1()
    while True:
        choice = input("What do you do? ")

        if choice == "look":
            ex36strings.trail1()
        
        elif choice in ["run", "flee", "retreat", "withdraw"]:
            print("\nYou turn tail and run back down the trail!")
            global coward
            coward = True
            base()
        
        elif ("draw" in choice and "sword" in choice) or choice in ["attack", "kill", "fight"]:
            global weapons_and_armor
            print("Your weapons and armor are",weapons_and_armor)

            if weapons_and_armor == "covered in ice!":
                ex36strings.fight_goblins_frozen()
                die()

            else:
                ex36strings.fight_goblins_thawed()
                trail2()

        elif choice == "quit":
            quit()

        else:
            print("What was that? Try something else.")


def trail2():
    ex36strings.trail2()
    while True:
        choice = input("What do you do? ")

        if choice == "look":
            ex36strings.trail2()

        elif ("look" in choice or "search" in choice) and ("goblins" in choice or "corpse" in choice):
            ex36strings.look_corpses()

        elif ("look" in choice or "search" in choice) and "holes" in choice:
            ex36strings.look_holes()
            global grappling_hook
            grappling_hook = True

        elif ("go" in choice or "climb" in choice) and "trail" in choice:
            print("\nYou continue up the trail higher into the mountains.")
            cliff1()

        elif choice == "quit":
            quit()

        else:
            print("What was that? Try something else.")


def cliff1():
    ex36strings.cliff1()
    while True:
        global on_rocks
        choice = input("What do you do? ")
        
        if choice == "look":
            ex36strings.cliff1()
        
        elif "look" in choice and "troll" in choice:
            ex36strings.look_troll()

        elif "look" in choice and "rocks" in choice:
            ex36strings.look_rocks()

        elif choice in ["attack", "kill", "fight"] and not on_rocks: 
            ex36strings.fight_off_rocks()
            die()
        
        elif choice in ["attack", "kill", "fight"] and on_rocks: 
            ex36strings.fight_on_rocks()
            cliff2()

        elif ("climb" in choice or "go" in choice) and "cliff" in choice:
            ex36strings.climb_cliff_troll()
            die()

        elif ("climb" in choice or "go" in choice) and "rocks" in choice:
            ex36strings.climb_rocks()
            on_rocks = True

        elif choice in ["run", "flee", "retreat", "withdraw"]:
            print("\nYou turn tail and run back down the trail!")
            global coward
            coward = True
            trail2()

        elif choice == "quit":
           quit()

        else:
            print("What was that? Try something else.")


def cliff2():
    ex36strings.cliff2()
    while True:
        global on_rocks
        choice = input("What do you do? ")
        
        if choice == "look":
            ex36strings.cliff2()

        elif "look" in choice and "remains" in choice:
            ex36strings.look_remains()

        elif "climb" in choice and not grappling_hook:
            ex36strings.climb_cliff_no_hook()
            die()

        elif "climb" in choice and grappling_hook:
            ex36strings.climb_cliff_with_hook()
            cave()

        elif choice == "quit":
            quit()

        else:
            print("What was that? Try something else.")


def cave():
    ex36strings.cave()
    while True:
        global coward
        choice = input("What do you do? ")

        if choice == "look":
            ex36strings.cave()
        
        elif "look" in choice and ("shrine" in choice or "altar" in choice):
            ex36strings.look_altar()
        
        elif "look" in choice and ("warriors" in choice or "statues" in choice):
            ex36strings.look_warriors()
        
        elif "look" in choice and "hammer" in choice:
            ex36strings.look_hammer()

        elif "get" in choice and "hammer" in choice and coward:

            die()
        
        elif "get" in choice and "hammer" in choice and not coward:
            ex36strings.get_hammer()
            input("Press any key to continue...")
            ex36strings.victory()

        elif choice == "quit":
            quit()

        else:
            print("What was that? Try something else.")


# Game Loop
game()