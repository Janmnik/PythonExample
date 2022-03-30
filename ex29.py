#Co jeśli...

people = 20
cats = 30
dogs = 15

if people < cats:
    print("Zbyt dużo kotów! Świat jest skazany na zagładę!")

if people > cats:
    print("Nie za dużo kotów! Świat jest ocalony!")

if people < dogs:
    print("Świat sie ślini!")

if people > dogs:
    print("Świat jest suchy!")

dogs += 5

if people >= dogs:
    print("Liczba ludzi jest większa lub równa liczbie psów.")

if people <= dogs:
    print("Liczba ludzi jest mniejsza lub równa liczbie psów.")

if people == dogs:
    print("Ludzie są psami.")

#1. Jak myślisz, co robi instrukcja if z kodem znajdującym się pod nią?
# Jeżeli jest spełnieniony warunek wykonuje się
#2. Dlaczego kod pod instrukcją if musi być wcięty o cztery spacje?
#Ponieważ w instrukcja warunkowych w języku python wstawia się wcięcie składające z czterech spacji, lub jednego tabulatora, aby wyodrębnić zawartość.
#3. Co się dzieje, jeśli kod nie jest wcięty?
#Wyskakuje błąd "IndentationError: expected an indented block" i program nie działa poprawnie
#4. Czy możesz wstawić w instrukcji if inne wyrażenia boolowskie z ćwiczenia 27.? tak
#5. Co się stanie, jeśli zmienisz początkowe wartości dla zmiennych people (ludzie), cats (koty) i dogs (psy)? zmienią się spełnione warunki
