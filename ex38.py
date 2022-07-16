#Operacje na listach
ten_things = "Jabłka Pomarańcze Wrony Telefon Światło Cukier"
print("Chwileczkę, na tej liście nie ma 10 elementów.")

stuff = ten_things.split(' ')

#print(stuff)

more_stuff=["Dzień", "Noc", "Frisbee", "Kukurydza", "Banan", "Dziewczyna", "Chłopak"]

while len(stuff) != 10:
  next_one = more_stuff.pop()
  print("Dodawanie: ", next_one)
  stuff.append(next_one)
  print(f"Teraz jest {len(stuff)} elementów.")

print("Teraz to mamy: ", stuff)

print("Zróbmy jeszcze parę rzeczy ze stuff.")

print(stuff[1])
print(stuff[-1]) #łał! nieźle ostatni eleement listy
#Wyświetlenie listy jakociąg znaków
print(' '.join(stuff))
print(stuff.pop())
print(' '.join(stuff)) #serio? super
print('#'.join(stuff[3:5])) #super hiper

#Tablica to też lista :)
