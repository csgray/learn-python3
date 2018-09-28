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

The battle ends with the last goblin's head rolling off of its shoulders and falling at your feet.""")
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
            print("""
Gross. The only thing that smells worse than a goblin's outsides is a goblin's insides, and thanks to your handy skill
at epic fights, there's a bunch of goblin insides now outside and steaming. You pick over the battlefield with a
practiced eye but don't find anything worth taking.
            """)

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
            print("""
You've faced many trolls on your journey here, but this troll is larger than them all. It's thick hide is covered with
scars and strong muscles ripple beneath. It wields a tree trunk like a club and lounges near the rocks at the base of
the cliff while waiting for its next meal.
            """)

        elif "look" in choice and "rocks" in choice:
            print("""
Rocks and boulders of various size lie around the base of the cliff, likely having fallen from the heights. They look
like they could be climbed to give you a higher vantage point.
            """)

        elif choice in ["attack", "kill", "fight"] and not on_rocks: 
            print("""
You charge towards the troll with your sword drawn and gleaming in the light! The beast swings its club at you, which
you deftly dodge to stab at it's flanks, but your blade fails to pierce its thick hide. The troll catches you with the
backswing, knocking you into the rocks, and you see it lift its club before it crushes your skull and you slip into
oblivion.
            """) 
            die()
        
        elif choice in ["attack", "kill", "fight"] and on_rocks: 
            print("""
With a mighty battle cry, you leap off of the rocks and onto the neck of the troll!  It had no idea that you were there,
waiting for the perfect moment to strike, and bellows in surprise as you land on its shoulders with your arms wrapped
around its neck. You dodge from shoulder to shoulder as it tries to grab you and stab at its neck, your sword slipping
off its thick hide, before you go for the really soft bits: Its eyes.

Sharp steel ruptures the gelatinous orb and now the troll screams in not rage but pain as it is half blinded. Another
blow finishes the job and it flails wildly, bashing into the rocks it can't see with its ruined eyes, while you
repeatedly drive your sword into face. Finally, in desperation, the troll swings its club at you and crushes its own
skull. The massive beast collapses, falling forward and landing in a puddle of its own blood, leaving you standing
victorious.""")
            cliff2()

        elif ("climb" in choice or "go" in choice) and "cliff" in choice:
            print("""
You try to run past the troll to scale the cliff, but it catches you by the leg. It lifts you into the air, ignoring
your wild swings with your sword, and grabs you by both legs to tear you in half.
            """)
            die()

        elif ("climb" in choice or "go" in choice) and "rocks" in choice:
            print("""
You manage to approach the rocks without being noticed by the troll. You scramble up the rough, icy surface to take a
position where you can look down on the troll.
            """)
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
            print("""
The bones of who knows how man would-be heroes are piled at the base of the cliff and scattered about the area. Some
clearly fell to the precipitous climb and others to the troll, but the end result is the same. Dozens of warriors lie
in ruins around you and their gear has long been lost to the elements.
            """)

        elif "climb" in choice and not grappling_hook:
            print("""
You walk to the base of the cliff and look up: Your goal is high above you and there don't seem to be many handholds,
but you're not about to let that stop you. You start to scale the sheer cliff, finding a few places to jam your fingers
and the toes of your boots, but halfway up you find an impass: There's nothing but blank rock between you and the next
handhold several feet above you.

You summon all your strength and launch yourself up the cliff face - only to fall short. Then you fall down the rest of
the cliff and break your neck.
            """)
            die()

        elif "climb" in choice and grappling_hook:
            print("""
You walk to the base of the cliff and look up: Your goal is high above you and there don't seem to be many handholds,
but you came prepated. You take out the grappling hook that you found earlier and spin it, building up momentum, then
launch it towards the cave mouth high overhead. There's the scraping of metal on rock before it catches somehere high
overhead. A few sharp tugs tells you that it is well anchored and you start your ascent.""")
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
            print("""
Carved from the stone of the cave itself and permanently fixed to the floor, this altar sits on a raised dais at the
back of the cave with curved ramps that hug the walls leading up to it. The sides depict images of epic battles where
heroes of centuries of old face demonic enemies. The top is bare save for the huge hammer on top of it.
            """)
        
        elif "look" in choice and ("warriors" in choice or "statues" in choice):
            print("""
Two grim warriors stand eternal guard over the altar. Every detail is reflected in their weapons and armor, and their
helmeted gaze is fixed on the hammer atop the altar. A dim blue glow is barely perceptible from within the helms.
            """)
        
        elif "look" in choice and "hammer" in choice:
            print("""
This massive hammer rests atop the altar waiting for a warrior with a heart pure of steel. An ancient weapon, the head
is a block of carved stone reinforced with metal and bearing runes. The haft is almost as long as a man is tall. The
very air surrounding the hammer thrums with a barely contained power from thousands of years ago.

This can only be the HAMMER OF GLORY!
            """)

        elif "get" in choice and "hammer" in choice and coward:
            print("""
The air feels heavy, thick even, as you approach the altar and you can't shake the feeling that something is watching
you. Judging you. Your heart is pounding in your ears as you reach for the HAMMER OF GLORY.

Time seems to stop when you touch the worn haft. "DEFILER!" booms a pair of thunderous voices. The sound seems to
emanage from within your head and the very walls of the cave all at once. "COWARD! ONLY A HERO WITH A HEART PURE OF
STEEL MAY CLAIM THE HAMMER OF GLORY!"

You try to remove your hand but can't as the flames in the sconces roar towards the ceiling and the eyes within the
helms of the stone warriors burn. The agony you feel is brief but intense as the ancient power of the HAMMER OF GLORY
turns against you and blasts you apart down to your atoms.
            """)
            die()
        
        elif "get" in choice and "hammer" in choice and not coward:
            print("""
The air feels heavy, thick even, as you approach the altar and you can't shake the feeling that something is watching
you. Judging you. Your heart is pounding in your ears as you reach for the HAMMER OF GLORY.

Time seems to stop when you touch the worn haft. The HAMMER OF GLORY seems to push against your hand and your mind, and
now you can feel the gaze of the stone warriors boring down into your soul. After what feels like an eternity of
scrutiny but is really only a few seconds, the presence relents and your fingers tighten around the haft.

The HAMMER OF GLORY is deceptively light in your hands, but you know that should you swing it it will come down with all
the force and wrath of the gods. This is the only weapon that can stand against Zargothrax and his army of undead
unicorns.

You raise it up to the heavens above, and you hail the king!
            """)
            input("Press any key to continue...")
            ex36strings.victory()

        elif choice == "quit":
            quit()

        else:
            print("What was that? Try something else.")


# Game Loop
game()