#znak zachęty i przekazywanie zmiennej
from sys import argv
#przekazanie argumentu zewnętrznego username oraz użycie nazwy obecnej skryptu 'ex14.py'
script, username = argv
promt = username+'> '

print(f"Cześć, {username}, jestem skryptem {script}.")
print("Chciałbym zadać Tobie parę pytań.")
print(f"Lubisz mnie, {username}?")
likes = input(promt)

print(f"Gdzie mieszkasz, {username}?")
lives = input(promt)

print("Jaki masz komputer?")
computer = input(promt)

print(f"""
Okay, gdy zapytałem, czy mnie lubisz, odpowiedziałeś {likes}.
Mieszkasz w  {lives}. Nie jestem pewien, gdzie to jest.
I masz komputer {computer}. Fajnie
""")
