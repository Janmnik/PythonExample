#Gałęzie i funkcje
from sys import exit

def gold_room():
    print("Ten pokój jest pełen złota. Ile złota zabierasz?")

    choice = input(">")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Stary, naucz się wpisywać liczby.")

    if how_much <50:
        print("Miło, nie jesteś chciwy, wygrywasz!")
        exit(0)
    else:
        dead("Ty chciwy draniu")

def bear_room():
    print("Jest tutaj niedźwiedź.")
    print("Niedźwiedź ma beczkę miodu.")
    print("Ten gruby niedźwiedź siedzi przed następnymi drzwiami.")
    print("Jak przesuniesz niedźwiedzia?")
    bear_moved = False
    
    while True:
        choice = input("> ")
        
        if choice == "zabieram miód":
            dead("Niedźwiedź spogląda na Ciebie i wali w twarz.")
        elif choice == "śmieję się z niedźwiedzia" and not bear_moved:
            dead("Niedźwiedź się wkurzył odgryzł Ci nogę.")
        elif choice == "otwieram drzwi" and bear_moved:
            gold_room()
        else:
            print("Nie mam pojęcia, co to znaczy.")

def cthulhu_room():
    print("Widzisz wielkiego Cthulu.")
    print("On znaczy to, nieważne, wpatruje się w Ciebie, a Ty popadasz w obłęd.")
    print("Ratujesz się ucieczką, czy zjadasz swoją głowę?")
    
    choice = input("> ")

    if "ucieczką" in choice:
        start()
    elif "głowę" or "zjadam głowę":
        dead("To było pyszne!")
    else:
        cthulhu_room()

def nothing_room():
    print("Widzisz nicość.")
    print("Czy uciekasz, a może nic robisz?")

    choice = input("> ")
    if "uciekam" in choice:
        start()
    elif "nic" in choice:
        start()
    else:
        nothing_room()

def dead(why):
    print(why, "Dobra robota!")
    exit(0)

def start():
    print("Znajdujesz się w mrocznym pokoju.")
    print("Po lewej i po prawej znajdują się drzwi.")
    print("Które wybierasz?")
    
    choice = input("> ")

    if choice == "lewe":
        bear_room()
    elif choice == "prawe":
        cthulhu_room()
    else:
        dead("Błąkasz sie po pokoju, aż w końcu umierasz z głodu.")

start()
