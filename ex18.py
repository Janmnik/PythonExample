#Nazwy, zmienne, kod i funkcje
#funkcje podobne do defininiowania skryptów z argv :)

def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

#Tylko *args jest właściwie bezcelowe i można z=pop prostu zrobić tak

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")


#funkcja przyjmująca jeden argument
def print_one(arg1):
    print(f"arg1: arg1")

#funkcja nie przyjmująca żadnych argumentów
def print_none():
    print("Ja nic nie mam.")

print_two("Jan", "Malec")
print_two_again("Jan", "Malec")
print_one("Pierwszy!")
print_none()

