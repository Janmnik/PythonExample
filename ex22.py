#baza wiedzy wiedzy
#ex1.py drukowanie, wyświetlanie tekstu
print("Ot tak drukowanie")
#ex2.py komentarze
#ex3.py tekst + działania
print("Wyświetlanie tekstu ", 2+3.1)
#ex4.py zmienne liczbowe
a=2
b=4
c=a*b
print("a + b = c ", a," + ",b," = ",c)
#ex5.py format String, tworzenie łańcucha znaków, formatowanie
zwierze ='Owiec'
liczba = 6
print(f"{zwierze} jest {liczba}")
#ex6.py pierwsze spotkanie sie z .format()
cebula = True
warstwa ="Cebula mma warstwy?! {}"
print(warstwa.format(cebula))
#ex7.py więcej drukowania
print("Drukowanie {}".format("tekstu."))
print("*"*10)
a = 'A'
b = 'L'
c = 'A'
print(a+b,c)
#ex8.py drukowanie formatter (sesja)
formatter = "{} {} {}"
print(formatter.format(1,0,1,1))
#ex9.py ciągi znaków
days ="Pon\n Wt\n Śr\n Cz Pt So N"
print(days)
print(""""test
test, test test""")
#ex10.py Co to było? Sekwencje ucieczki
print("Sekwencje ucieczki\n")
print("\\   \' \" \a tekst \b tekst tekst \f tekst \r tekst2")
#ex11.py  Zadawanie pytań
print("Podaj liczbę")
x = int(input())
#ex12.py wyswitlanie podpowiedzi użytkownikowi
response = input("Czy lubisz ankiety?")
print("Można? ", input())
#ex13.py parametry rozpakowanie zmienne
from sys import argv
script, parametr = argv
print("skrypt nazywa się",script)
print(f"Parametr skryptu: {parametr}")
#ex14.py znak zachęty i przekazywanie zmiennej
promt = parametr+'< '
print(promt," Jak się masz?")
#ex15.py Czytanie z pliku
filename = input("Podaj nazwe pliku")
txt = open(filename)
print(txt.read())
#ex16.py Czytanie pliku i zapisanie
target = open(filename, 'w')
target.truncate()
target.write("t\n")
target.close()
#ex17.py kopiowanie więcej plików
#ex18.py Nazwy, zmienne, kod i funkcje
def function(arg1, arg2):
    print(f"Argumenty {arg1} i {arg2}")
def functionNone():
    print("None")
#ex19.py Funkcje i zmienne
a = 1
b = 3
function(a, b+4)
def Welcome(name):
    print(f"Witaj {name}!")
#ex20.py Funkcje i pliki
def print_all(f):
    print(f.read())
def rewind(f):
    f.seek(0);
#ex21.py Funkcje mogą coś zwracać
def add(a, b):
    return a+b
add(1,2)



