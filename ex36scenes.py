# Corey Gray
# ex36scenes.py
# The scenes for ex36.py because these multi-line strings are unwieldy in the game engine code.

from sys import exit

def intro():
    print(r"""
You are the prince of the land of Fife, noble and true with a heart of steel - but the evil wizard Zargothrax invaded
Dundee with his army of undead unicorns. Fireballs and lightning rained from the sky while all the people died and
buildings collapsed to the floor. The beautiful princess Iona McDougall was taken to prison with cry and waits, frozen,
to die. You escaped, swearing the mighty oath, "I will make Zargothrax die!"

As revealed to you in a vision while sleeping in the woods near Glenrothes, you need three artifacts to defeat the
sorcerer: A golden dragon, a strange glowing amulet, and a huge enchanted hammer of war. And so begins the
                                       _______           _______  _______ _________
                                      (  ___  )|\     /|(  ____ \(  ____ \\__   __/
                                      | (   ) || )   ( || (    \/| (    \/   ) (   
                                      | |   | || |   | || (__    | (_____    | |   
                                      | |   | || |   | ||  __)   (_____  )   | |   
                                      | | /\| || |   | || (            ) |   | |   
                                      | (_\ \ || (___) || (____/\/\____) |   | |   
                                      (____\/_)(_______)(_______/\_______)   )_(   

                                                        FOR  THE
          _______  _______  _______  _______  _______    _______  _______    _______  _        _______  _______          
|\     /|(  ___  )(       )(       )(  ____ \(  ____ )  (  ___  )(  ____ \  (  ____ \( \      (  ___  )(  ____ )|\     /|
| )   ( || (   ) || () () || () () || (    \/| (    )|  | (   ) || (    \/  | (    \/| (      | (   ) || (    )|( \   / )
| (___) || (___) || || || || || || || (__    | (____)|  | |   | || (__      | |      | |      | |   | || (____)| \ (_) / 
|  ___  ||  ___  || |(_)| || |(_)| ||  __)   |     __)  | |   | ||  __)     | | ____ | |      | |   | ||     __)  \   /  
| (   ) || (   ) || |   | || |   | || (      | (\ (     | |   | || (        | | \_  )| |      | |   | || (\ (      ) (   
| )   ( || )   ( || )   ( || )   ( || (____/\| ) \ \__  | (___) || )        | (___) || (____/\| (___) || ) \ \__   | |   
|/     \||/     \||/     \||/     \|(_______/|/   \__/  (_______)|/         (_______)(_______/(_______)|/   \__/   \_/  
""")

def base():
    print(r"""
The snow keeps on falling as you ride to the north. You started your journey to the faraway mountains weeks ago, and now
your destination is in sight: The tallest mountain where, it is said, in a cave on the mountain up high there is a
mystical shrine containing the HAMMER OF GLORY!

You have fought many goblins and trolls to get here, but now your armor and weapons are covered in ice and there is no
telling what dangers you will face ascending the mountain. At the base of the mountain, you dismount and tie up your
horse in a sheltered alcove. There's a small pile of dry wood, good for a fire, likely left over from a previous camp.
A narrow, winding trail is barely visible through the falling snow.
    """)

def trail1():
    print(r"""
The trail winds through a narrow passage between two ice-covered boulders then through a thick copse of birch trees.
It's dark here, the trees blocking much of the light, and quiet. Too quiet. The only sound you can hear is the sound of
your own boots crunching in the deep snow.

Suddenly, you hear high-pitched shouting and a gang of goblins burst out of the snow, throwing back the stand that they
were hiding under with a spray of snow. They draw their impractical swords and rush towards you!
    """)

def trail2():
    print(r"""
Numerous goblin corpses and pieces of corpses litter this clearing in the birch forest along with a motley collection of
impractical swords. A thick, almost syrupy slush comprised of snow and goblin blood squishes under your heavy boots.
Several holes at the bases of nearby trees reveal where the goblins were lying in ambush, and the trail leading higher
up the mountain continues at the far end of the clearing.   
    """)

def cliff1():
    print(r"""
The trail ends at the base of a sheer cliff below a cave set into the mountainside. Bones and broken weapons and armor
litter the ground - and the reason is soon apparent: A massive troll, larger than any that you have seen before, lounges
against the rocks near the cliff. Fortunately, it hasn't seen you yet.
    """)

def cliff2():
    print(r"""
A massive troll lies face down in a puddle of its own blood, and the way to the base of the cliff is clear. Set high
into the mountain overhead is a cave, and the remains of numerous would-be heroes lies at the base of the cliff.
    """)

def cave():
    print(r"""
This is a cave on a mountain up high. While the entrance is rough and the wind howls near the mouth, the interior of the
cave gradually transitions to finished stonework. Sconces carved into the walls burn with an undying blue flame that
banish all shadows from the shrine. For it is a shrine: At the far end of the cave, a large stone altar rises out of the
ground. Two large stone warriors flank the shrine gazing down at a huge hammer atop the shrine.
    """)

def quit():
    print(r"""
You quit the quest. Dundee remains a ruin, the princess Iona McDougall remains frozen, and Zargothrax reigns forever
as the new dark master of Fife.
    """)
    exit()

def victory():
    print(r"""
Armed with the HAMMER OF GLORY, you descend from the mountain to continue your quest. No power imaginable can stand
against the HAMMER OF GLORY's epic might, but you need two more artifacts if you are to free the princess Iona
McDougall and restore cosmic balance to the lands of Dundee: A magic, golden dragon and the AMULET OF JUSTICE.

None may doubt your worth. You are truly the ultimate fighter and a hero with a heart pure of steel!
    """)
    exit()