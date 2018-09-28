# Corey Gray
# ex36strings.py
# The strings for ex36.py because these multi-line strings are unwieldy in the game engine code.

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

# Strings for the base camp scene
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

def look_trail():
    print(r"""
Calling this narrow, winding path a 'trail' may be a bit generous, but there is a clear break in the snow-covered rocks
leading further up the mountain.
    """)

def light_fire():
    print(r"""
You light a fire in the sheltered alcove. Not only does your horse seem to appreciate it, but your weapons and armor
thaw out. Water slowly runs down the hard metal surfaces to coalesce in a pool around your feet, which is kind of
annoying, but you find it easier to move. Plus, you can actually draw your sword!
    """)

# Strings for the first trail scene
def trail1():
    print(r"""
The trail winds through a narrow passage between two ice-covered boulders then through a thick copse of birch trees.
It's dark here, the trees blocking much of the light, and quiet. Too quiet. The only sound you can hear is the sound of
your own boots crunching in the deep snow.

Suddenly, you hear high-pitched shouting and a gang of goblins burst out of the snow, throwing back the stand that they
were hiding under with a spray of snow. They draw their impractical swords and rush towards you!
    """)

def fight_goblins_frozen():
    print(r"""
You try to draw your sword and fight the minuscule goblins, but your sword is frozen to its scabbard. While you fumble
with the hilt, the goblins swarm over you and stab you repeatedly in the face.
    """)

def fight_goblins_thawed():
    print(r"""
You draw your sword from its weatherworn sheath and an epic battle is fight! The creatures are as weak as they are evil
and they swing their oversized blades in wide, slow arcs, but for every goblin that you cut down it seems two more
spring from some hole in the snow to join the fray. Soon their black blood covers the snow, which has been churned into
a thick slush beneath your boots, and the sound of steel on steel echos through the mountains.

The battle ends with the last goblin's head rolling off of its shoulders and falling at your feet.""")

# Strings for the second trail scene
def trail2():
    print(r"""
Numerous goblin corpses and pieces of corpses litter this clearing in the birch forest along with a motley collection of
impractical swords. A thick, almost syrupy slush comprised of snow and goblin blood squishes under your heavy boots.
Several holes at the bases of nearby trees reveal where the goblins were lying in ambush, and the trail leading higher
up the mountain continues at the far end of the clearing.   
    """)

def look_corpses():
    print(r"""
Gross. The only thing that smells worse than a goblin's outsides is a goblin's insides, and thanks to your handy skill
at epic fights, there's a bunch of goblin insides now outside and steaming. You pick over the battlefield with a
practiced eye but don't find anything worth taking.
    """)

def look_holes():
    print(r"""
There are multiple holes at the base of the trees surrounding the clearing which lead to a maze of tunnels which are
too short to move through. That and they smell like something died. Many somethings died. Most of the holes are filled
with worthless trash, but in one of them you find an adventurer's pack containing a grappling hook.
    """)

# Strings for the first cliff scene
def cliff1():
    print(r"""
The trail ends at the base of a sheer cliff below a cave set into the mountainside. Bones and broken weapons and armor
litter the ground - and the reason is soon apparent: A massive troll, larger than any that you have seen before, lounges
against the rocks near the cliff. Fortunately, it hasn't seen you yet.
    """)

def look_troll():
    print(r"""
You've faced many trolls on your journey here, but this troll is larger than them all. It's thick hide is covered with
scars and strong muscles ripple beneath. It wields a tree trunk like a club and lounges near the rocks at the base of
the cliff while waiting for its next meal.
    """)

def look_rocks():
    print(r"""
Rocks and boulders of various size lie around the base of the cliff, likely having fallen from the heights. They look
like they could be climbed to give you a higher vantage point.
    """)

def fight_off_rocks():
    print(r"""
You charge towards the troll with your sword drawn and gleaming in the light! The beast swings its club at you, which
you deftly dodge to stab at it's flanks, but your blade fails to pierce its thick hide. The troll catches you with the
backswing, knocking you into the rocks, and you see it lift its club before it crushes your skull and you slip into
oblivion.
    """)

def fight_on_rocks():
    print(r"""
With a mighty battle cry, you leap off of the rocks and onto the neck of the troll!  It had no idea that you were there,
waiting for the perfect moment to strike, and bellows in surprise as you land on its shoulders with your arms wrapped
around its neck. You dodge from shoulder to shoulder as it tries to grab you and stab at its neck, your sword slipping
off its thick hide, before you go for the really soft bits: Its eyes.

Sharp steel ruptures the gelatinous orb and now the troll screams in not rage but pain as it is half blinded. Another
blow finishes the job and it flails wildly, bashing into the rocks it can't see with its ruined eyes, while you
repeatedly drive your sword into face. Finally, in desperation, the troll swings its club at you and crushes its own
skull. The massive beast collapses, falling forward and landing in a puddle of its own blood, leaving you standing
victorious.""")

def climb_cliff_troll():
    print(r"""
You try to run past the troll to scale the cliff, but it catches you by the leg. It lifts you into the air, ignoring
your wild swings with your sword, and grabs you by both legs to tear you in half.
    """)

def climb_rocks():
    print(r"""
You manage to approach the rocks without being noticed by the troll. You scramble up the rough, icy surface to take a
position where you can look down on the troll.
    """)

# Strings for the second cliff scene
def cliff2():
    print(r"""
A massive troll lies face down in a puddle of its own blood, and the way to the base of the cliff is clear. Set high
into the mountain overhead is a cave, and the remains of numerous would-be heroes lies at the base of the cliff.
    """)

def look_remains():
    print(r"""
The bones of who knows how man would-be heroes are piled at the base of the cliff and scattered about the area. Some
clearly fell to the precipitous climb and others to the troll, but the end result is the same. Dozens of warriors lie
in ruins around you and their gear has long been lost to the elements.
    """)

def climb_cliff_no_hook():
    print(r"""
You walk to the base of the cliff and look up: Your goal is high above you and there don't seem to be many handholds,
but you're not about to let that stop you. You start to scale the sheer cliff, finding a few places to jam your fingers
and the toes of your boots, but halfway up you find an impass: There's nothing but blank rock between you and the next
handhold several feet above you.

You summon all your strength and launch yourself up the cliff face - only to fall short. Then you fall down the rest of
the cliff and break your neck.
    """)

def climb_cliff_with_hook():
    print(r"""
You walk to the base of the cliff and look up: Your goal is high above you and there don't seem to be many handholds,
but you came prepated. You take out the grappling hook that you found earlier and spin it, building up momentum, then
launch it towards the cave mouth high overhead. There's the scraping of metal on rock before it catches somehere high
overhead. A few sharp tugs tells you that it is well anchored and you start your ascent.""")

# Strings for the cave scene
def cave():
    print(r"""
This is a cave on a mountain up high. While the entrance is rough and the wind howls near the mouth, the interior of the
cave gradually transitions to finished stonework. Sconces carved into the walls burn with an undying blue flame that
banish all shadows from the shrine. For it is a shrine: At the far end of the cave, a large stone altar rises out of the
ground. Two large stone warriors flank the shrine gazing down at a huge hammer atop the shrine.
    """)

def look_altar():
    print(r"""
Carved from the stone of the cave itself and permanently fixed to the floor, this altar sits on a raised dais at the
back of the cave with curved ramps that hug the walls leading up to it. The sides depict images of epic battles where
heroes of centuries of old face demonic enemies. The top is bare save for the huge hammer on top of it.
    """)

def look_warriors():
    print(r"""
Two grim warriors stand eternal guard over the altar. Every detail is reflected in their weapons and armor, and their
helmeted gaze is fixed on the hammer atop the altar. A dim blue glow is barely perceptible from within the helms.
    """)

def look_hammer():
    print(r"""
This massive hammer rests atop the altar waiting for a warrior with a heart pure of steel. An ancient weapon, the head
is a block of carved stone reinforced with metal and bearing runes. The haft is almost as long as a man is tall. The
very air surrounding the hammer thrums with a barely contained power from thousands of years ago.

This can only be the HAMMER OF GLORY!
    """)

def get_hammer_coward():
    print(r"""
The air feels heavy, thick even, as you approach the altar and you can't shake the feeling that something is watching
you. Judging you. Your heart is pounding in your ears as you reach for the HAMMER OF GLORY.

Time seems to stop when you touch the worn haft. "DEFILER!" booms a pair of thunderous voices. The sound seems to
emanage from within your head and the very walls of the cave all at once. "COWARD! ONLY A HERO WITH A HEART PURE OF
STEEL MAY CLAIM THE HAMMER OF GLORY!"

You try to remove your hand but can't as the flames in the sconces roar towards the ceiling and the eyes within the
helms of the stone warriors burn. The agony you feel is brief but intense as the ancient power of the HAMMER OF GLORY
turns against you and blasts you apart down to your atoms.
    """)

def get_hammer():
    print(r"""
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

# Strings for game functions
def quit():
    print(r"""
You quit the quest. Dundee remains a ruin, the princess Iona McDougall remains frozen, and Zargothrax reigns forever
as the new dark master of Fife.
    """)

def victory():
    print(r"""
Armed with the HAMMER OF GLORY, you descend from the mountain to continue your quest. No power imaginable can stand
against the HAMMER OF GLORY's epic might, but you need two more artifacts if you are to free the princess Iona
McDougall and restore cosmic balance to the lands of Dundee: A magic, golden dragon and the AMULET OF JUSTICE.

None may doubt your worth. You are truly the ultimate fighter and a hero with a heart pure of steel!
    """)
    exit()