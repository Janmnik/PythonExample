#Parametry, rozpakowanie i zmienne
#importowanie
from sys import argv
#instrukcje uruchomienia znajdziesz w rozdziale "Co powinien zobaczyć"
script, first, second, third, pseudomin = argv

print("Ten skrypt nazywa się:", script)
print("Ten skrypt nazywa się:", first)
print("Ten skrypt nazywa się:", second)
print("Ten skrypt nazywa się:", third)
print("imię:")
imie = input()
nazwisko = input("nazwisko: ")
print(f"Nazywasz się {imie} {nazwisko} {pseudomin}")
