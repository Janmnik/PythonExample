#Moduły, klasy obiekty
class Song(object):
  def __init__(self, lyrics):
    self.lyrics = lyrics
  
  def sing_me_a_song(self):
    for line in self.lyrics:
      print (line)

  def sing_me_word(self):
    print (self.lyrics)

happy_bday = Song(["Happy birthady to you",
                  "Nie chce zostac pozwany",
                  "Więc tutaj przerwę"])

bulls_on_parade = Song(["They rally around the familly",
                       "With pockets full of shells"])

a_spoon_of_sugar = Song(["Spoon of sugar",
                        "to medicine go down",
                        "to medicine go down",
                        "and again"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
a_spoon_of_sugar.sing_me_a_song()

test_song = "Testowo owo piosenka..."
test_song.sing_me_word()