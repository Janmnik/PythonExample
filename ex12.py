#Wyświetlanie podpowiedzi dla użytkownika
x = input("Imie? ")
y = input("Nazwisko? ")
age = input("Ile masz lat? ")
height = input("Ile masz wzrostu? ")
#zapytanie się Ile ważysz i przekazanie zmennej w tym samym wierszu
weight = input("Ile ważysz? ")

print(f"Witaj {x} {y}, masz {age} lat, {height} wzrostu i ważysz {weight}.")
#brak przypisania do zmiennej input()
print("Ile masz lat?", input())
