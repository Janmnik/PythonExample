#Czytanie z plików
from sys import argv
#zmienne script - zmienna przechowującą nazwę obecnego pliku ,filename zmienna zewnętrzna
script, filename = argv
#tworzy obiekt pliku
txt = open(filename)
#Drukuje wybrany plik do utworzenia
print(f"Oto twój plik {filename}:")
#Czytanie pliku 
print(txt.read())

print("Wpisz ponownie nazwę pliku:")
#przypisanie informacji z klawiatury o zmiennej
file_again = input("> ")
#utworzenie obiektu txt_again
txt_again = open(file_again)

print(txt_again.read())
print(f"A to był twój Skrypt: {script}")
