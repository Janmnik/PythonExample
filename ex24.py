#Więcej praktyki
print("Przećwiczmy wszystko.")
print('Musisz poćwiczyć sekwencje ucieczki ze znakiem \\, które wstawiają:')
print('\n nowe linie oraz \t tabultor.')
poem = """
\tTen piękny świat
z tak mocno osadzoną logiką
nie potrafi dostrzec \n potrzeby miłości
ani pojąc pasji płynącej z przeczucia
i wymaga wyjaśnienia
\n\t\tale żadnego nie ma.
"""

print("------------------------")
print(poem)
print("------------------------")

five = 10 - 2 + 3 - 6
print(f"To powinno wynosić pięć: {five}")


def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 1000

