#pierwsze spotkanie się z .format()
#inicjacja zmiennej types_of_people
types_of_people=10
#Przpisanie ciągu znaka=ów do zmiennej x
x = f"Istnieje {types_of_people} rodzajów ludzi."
#przypisanie zmiennej wartości string
binary = "binarny"
#tu też przypisanie zmiennej wartości string
do_not = "nie znają"
#przypisanie wartości string do zmiennnej y z zagnieżdżonymi stringami
y = f"Ci, którzy znają system {binary} i ci, którzy go {do_not}."
#drukuj x na ekran konsoli
print(x)
#drukuj y na ekran konsoli
print(y)
# wydrukowanie w konsoli Stringa z zagniżdżonym stringiem(z ciągiem znaków)
print(f"Powiedziałem: {x}")
print(f"Powiedziałem również: '{y}'")
#Przypisanie zmiennej hilarious wartość boolowską (logiczną)false
hilarious = False
joke_evaluation = "Czy to nie jest przezabawny dowcip?! {}"
#.format() pozwala wyświtlić zmienne w ciągu znaków
print(joke_evaluation.format(hilarious))

w = "To jest lewa strona..."
e = "łąńcucha znaków z prawą strona"

print(w+e+" "+binary)


#print("Tutaj jest tesowy tekst")
