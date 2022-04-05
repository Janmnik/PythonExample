#Podejmowanie decyzji
import time
print("""Wchodzisz do ciemnego pokoju z dwoma drzwiami.
Przechodzisz przez drzwi nr 1 czy nr 2? """)
door = input("> ")

if door =="1":
    print("Widzisz tam wielkiego niedźwiedzia, który zjada sernik.")
    time.sleep(5)
    print("Co robisz?")
    print("1. Zjadasz sernik?")
    print("2. Krzyczysz na niedźwiedzia.")
    
    bear = input("> ")

    if bear == "1":
        print("Niedźwiedź odgryza Ci nos. Dobra robota!")
    elif bear == "2":
        print("Niedźwiedź odgryza Ci nogi. Dobra robota!")
    else:
        print(f"Cóż, {bear} to prawdopodobnie lepszy wybór.")
        print("Niedźwiedź ucieka.")

elif door == "2":
    print("Wpatrujesz sie w nieskończoną otchłań oka Cthulu.")
    time.sleep(1)
    print("1. Jagody")
    time.sleep(1)
    print("2. Żółte spinacze do bielizny.")
    time.sleep(1)
    print("3. Wyruzumiałe rewolwery nucą melodie.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Twoje ciało ocalało, ale mózg masz jak galaretka owocowa.")
        print("Dobra robota!")
    else:
        print("Z szaleństwa gniją Ci oczy i zamieniają się w kałużę błota.")
        print("Dobra robota!")
elif door == "3":
    print("Spotykasz dużego robota Clanka.")
    print("Co robisz?")
    print("1. Patrzysz sie na niego.")
    print("2. Próbujesz go zniszczyć.")
    robot = input("> ")
    if robot == "1":
        print("Zostaje z Ciebie ciasto truskawkowe.")
        print("Dobra robota!")
    elif robot == "2" or robot == "3":
        print("Wyszedłeś cało, robot zwariował patrząc się na Ciebie.")
        print("Dobra robota!")
    else:
        print("Wypalasz się!")
        print("Dobra robota!")

else:
    print("Potykasz się, nadziewasz się na nóż i umierasz. Dobra robota!")
