class Song(object):
    
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

crail = ["HAIL! TO CRAIL!",
         "Mightiest warriors in the land",
         "HAIL! TO CRAIL!",
         "Ready to fight with a sword in hand"]

# Make a copy otherwise it is passed by reference and later modifications to crail change the song.
hail = Song(crail.copy())

# Like this. This was messing up hail.
crail.reverse()

# Another way to copy a list/sequence is by passing it as a slice.
# Also can't do 'laih = Song(crail.reverse())' as that, while modifying crail, is a None type.
laih = Song(crail[:])

print('-' * 10)
hail.sing_me_a_song()
print('-' * 10)
laih.sing_me_a_song()