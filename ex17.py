#Więcej plików (kopiowanie więcej plików)
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"kopiowanie z {from_file} do {to_file}")

#Moglibyśmy zrobić te dwie rzeczy w jednej lini? jak? Nie, to zależy od definicji jednej lini kodu.
in_file = open(from_file)
indata = in_file.read()


print(f"Plik wejściowy  ma {len(indata)} bajtów")

print(f"Czy plik wyjściowy istnieje? {exists(to_file)}")
print("Wciśnij RETURN, aby kontynować lub CTRL+C, aby anulować.")
input()

#Utworzenie pliku do zapisu i następnie zapisanie łancucha znaków zmiennej indata
out_file = open(to_file, 'w')
out_file.write(indata)

print("W porządku zrobione.")

#zamknięcie plików
out_file.close()
in_file.close()

