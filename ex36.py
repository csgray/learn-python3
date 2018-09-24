# Corey Gray
# ex36.py - Designing and Debugging... An Adventure Game!
# A really simple text adventure using lists, functions, and modules (No objects!)

import ex36scenes # for scene descriptions

weapons_and_armor = "covered in ice!"

ex36scenes.intro()
input("Press any key to continue...")

ex36scenes.base()
while True:
    choice = input("What do you do? ")

    if choice == "look":
        ex36scenes.base()

    elif choice == "light a fire":
        print("""
You light a fire in the sheltered alcove. Not only does your horse seem to appreciate it, but your weapons and armor
thaw out. Water slowly runs down the hard metal surfaces to coalesce in a pool around your feet, which is kind of
annoying, but you find it easier to move. Plus, you can actually draw your sword!
        """)
        weapons_and_armor = "thawed!"
    
    elif choice == "quit":
        ex36scenes.quit()

    else:
        print("What was that? Try something else.")