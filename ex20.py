#Funkcje i pliki

from sys import argv
#argumenty skryptu
script, input_file = argv

#metoda print_all czytająca plik
def print_all(f):
    print(f.read())

#metoda służąca do powrotu do początku pliku na 0 bajt
def rewind(f):
    f.seek(0)

#metoda do odczytania jednej lini
def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("Najpierw wydrukujemy cały plik:\n")
print_all(current_file)

print("Teraz przewińmy do tyłu, tak jak przewija sie kasetę.")
#powrót do początku pliku
rewind(current_file)

print("Wydrukujemy trzy linie:")
for x in range(1, 4):
    current_line = x
    print_a_line(current_line, current_file)

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)




