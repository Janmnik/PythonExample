#Funkcje mogą coś zwracać

def add(a, b):
    print(f"Dodawanie {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"Odejmowanie {a} - {b}")
    return a-b

def multiply(a, b):
    print(f"Mnożenie {a} * {b}")
    return a * b

def divide(a, b):
    print(f"Dzielenie {a} / {b}")
    return a / b
def expenentiationS(a, b):
    print(f"Potęgowanie {a} ^ {b}")
    return a**b

def expenentiation(a, b):
    print(f"Potęgowanie {a} ^ {b}")
    c=a
    for x in range(0,b-1):
        c = c * a
        print(f"a: {c}")
    return c

print("Wykonajmy kilka operacji aretmetycznych")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Wiek: {age}, Wzrost: {height}, Waga: {weight}, IQ: {iq}")
print("Można też potęgować")
print("Wynik: ",expenentiation(float(input("Podaj postawę: ")), int(input("Podaj potęgę: "))))

#łamigłówka
print("Oto zadanie.")
# age+ height- (weight * iq/2)
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print("To daje:", what, "Czy dałbyś obilczyc to ręcznie?")
print(age+height-(weight*iq/2))
