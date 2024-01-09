class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing(self):
        for line in self.lyrics:
            print(line)
        print("")
    
    def meta(self):
        print("\tArtist: %s, Year: %s" % (self.artist, self.year))
    
    def artist(self, artist):
        self.artist = artist
    
    def year(self, year):
        self.year = year

happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

happy_bday.year, happy_bday.artist = 1988, "Unknown"

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

shoes = Song(["Long ago and far away",
                "I went in a pair of shoes",
                "It took so long for me to say",
                "Everything you ask me too"])

# call
happy_bday.sing()
happy_bday.meta()

bulls_on_parade.sing()

shoes.sing()
