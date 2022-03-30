#Else oraz if
#people = 30
#cars = 40
#trucks = 15
people = input("Podaj ilość ludzi: ")
cars = input("Podaj ilość samochodów: ")
trucks = input("Podaj ilość ciężarówek: ")
if cars > people:
    print("Powinniśmy jechać samochodem.")
elif cars < people:
    print("Nie powinniśmy jechać samochadami.")
else:
    print("Nadal nie możemy się zdecydować.")

if trucks < cars:
    print("Może powinniśmy wziąć ciężarówki.")
else:
    print("Nadal nie możemy się zdecydować.")

if people > trucks:
    print("W porządku weźmy ciężarówki.")
else:
    print("W takim razie zostajemy w domu.")

if people or cars:
    print("To idziemy.")
else:
    print("Nie idziemy.")
#instrukcje elif else odpowiadają za wykonanie warunku przeciwnego do głównego warunku if definiowanego
