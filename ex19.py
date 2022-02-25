import datetime
#Funkcje i zmienne
#zdefiniowanie funkcji o dwóch parametrach
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"Masz {cheese_count} kawałków sera!")
    print(f"Masz {boxes_of_crackers} paczek krakersów!")
    print(f"Stary, to wystarczy, żeby zrobić imprezę!")
    print("Zorgnizuj sobie koc.\n")

print("Możemy po prostu bezpośrednio podać funkcji liczby:")
cheese_and_crackers(20,30)

print("Albo możemy użyć zmiennych ze skryptu:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("Możemy również wykonać wewnątrz operacje arytmetyczne:")
cheese_and_crackers(10+20, 5+6)

print("I możemy połączyć te dwie rzeczy, czyli zmienne i operacje arytmetyczne:")
#wywołanie funkcji z parametrami zmiennne z opracją artymetyczną dodawnaie
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 50)


def Welcome(name, surname):
    print(f"Witaj {name} {surname}!")
def Birthday(years):
    yearNow = int(datetime.datetime.now().year)
    print(f"Masz {yearNow-int(years)} lat")

print("Można też takie funkcje wywołać: ")
Welcome(input("Jak się nazywasz?\n"),input("Jakie masz nazwisko?\n"))
Birthday(input("W jakim roku sie urodziłeś? "))
