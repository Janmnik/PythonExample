#Pętle while
i = 0 
numbers = []

def AddToList(quantity):
    i = 0
    while i < quantity:
        numbers.append(i)
        i = i + 1
    return numbers

def AddToList2(quantity):
    for i in range(quantity):
        numbers.append(i)


while i < 6:
    print(f"Na górze i ma wartość {i}")
    numbers.append(i)
    
    i = i + 1
    print("Aktualne liczby: ", numbers)
    print(f"Na dole i ma wartość {i}")
print(AddToList(6))
