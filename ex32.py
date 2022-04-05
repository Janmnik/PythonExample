#Pętle i listy
the_count = [1,2,3,4,5]
fruits = ['jabłka', 'pomarańcze', 'gruszki', 'morele']
change = [1, 'jednogroszówki', 2, 'dwugroszówki', 3, 'pięciogroszówki']
#to jest pierwszy rodzaj pętli for, która przechodzi przez listę
for number in the_count:
    print(f"To jest licba {number}")

#to samo co wyżej
for fruit in fruits:
    print(f"Rodzaje owocu: {fruit}")

#możemy również przechodzić przez listy mieszane
#zwróć uwagę, że musimy uzyć {}, ponieważ nie wiemy co wniej jest
for i in change:
    print(f"Mam {i}")

#możemy również budować listy, zaczniemy od pustej
elements = []
for i  in range(0, 6):
    print(f"Dodajmy {i} do listy.")
    #append dodanie elementu na koniec (jest to funkcja którą listy rozumieją)
    elements.append(i)
#teraz możemy je wydrukować
for i in elements:
    print(f"Tym elementem było: {i}")

#określenie ilość elementów listy
print("ilośc elementów listy: "+str(len(elements)))
#metoda insert() dodadnia elementu o określonym ideksie
elements.insert(2, 22)
print(f"insert(2, 22) {elements}")
#metoda remove() usunięcie z listy określonego elementu
elements.remove(2)
print(f"remove(2) {elements}")
#metoda pop() usunięcie określonego indeksu
elements.pop(2)
print(f"pop(2) {elements}")
#metoda copy() skopiowianie listy
new_elements = elements.copy()
#metoda list() skopiowanie listy
new_elements = list(elements)
print(new_elements)
#clear wyczyszczenie listy
elements.clear()
print(elements)
