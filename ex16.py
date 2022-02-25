#Czytanie i zapisywanie plików
from sys import argv
# zmienna plikowe filename, script(nazwa skryptu obecnego)
script, filename = argv

print(f"Wymażemy {filename}")
print("Jeśli tego nie chcesz, wciśnij CTRL+C (^C).")
print("Jeśli tego chcesz, wciśnij RETURN.")

input("?")
print("Otwieranie pliku..")
#otwarcie pliku do zapisu
target = open(filename, 'w')
print("Wykasowanie pliku. Do widzenia!")
#opróżnia plik
target.truncate()
print("Teraz proszę Cię o wpisanie trzech lini tekstu.")

line1 = input("linia 1: ")
line2 = input("linia 2: ")
line3 = input("linia 3: ")

print("Zapisze je do pliku.")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("A na koniec zamykamy plik")
target.close()


