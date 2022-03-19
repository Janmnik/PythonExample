#Funkcje mogą coś zwracać
import time
start_time = time.time()

def add(a, b):
    print(f"Dodawanie {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"Odejmowanie {a} - {b}")
    return a-b

def multiply(a, b):
    print(f"Mnożenie {a} * {b}")
    #print(time.time()-start_time)
    return a * b

def multiplyA(a, b):
    print(f"Mnożenie {a} * {b}")
    result=0
    for x in range(0,b):
        result+=a
    #print(time.time()-start_time)
    return result

def divide(a, b):
    print(f"Dzielenie {a} / {b}")
    return a / b
def divideA(a, b):
    print(f"Dzielenie {a} / {b}")
    result = a
    i=0
    if a>b:
        while result!=0:
            #a = a-b
            result= result-b
            #print(f"r: {result}")
            i +=1
    else:
        return str(a)+"/"+str(b)
    return i

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

def expenentiationA(a, b):
    print(f"Potęgowanie {a} ^ {b}")
    c=a
    for x in range(0,b-1):
        c = multiplyA(c,a)
        print(f"a: {c}")
    return c
'''
print(multiply(40,20))
print("------------")
print(multiplyA(40,20))
print(divideA(4,2))
print(divideA(2,4))

'''
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
