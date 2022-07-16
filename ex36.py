#Moja własna gra

plecak=[]

def Backpack():
    if plecak != []:
        print("zawartość plecaka:")
        print(plecak)
    else:
        print("plecak jet niestety pusty. upss")


def AddToInventory(thing):
    plecak.append(thing)
    

def redroom():
    print("Widzisz niebieskie jagody, co robisz?")
    
    choice=input("> ")
    if choice == "Zabieram":
        print("zabierasz przedmiot do plecaka")
    elif choice == "zjadam":
        dead("O nie! Zatruwasz się i umierasz. Trucizna była zbyt mocna.")    

def blueroom():
    print("Ojej, to tylko twój podróżny przewodnik...")
    print("Co porabiasz?")
    choice=input("> ")

    

def yellowroom():
    print("Zielony pokój.")
    print("Znajdujesz zielony dywan, co robisz?")
    choice == input("> ")
    if choice == "Zabieram":
        print("Zabrane")
        
def greenroom():
    print("Zielony pokój.")

def dead(why):
        print(why, "Dobra robota!")

def start():
    print("Witaj podróżniku!")
    print("W ekwipunku masz przy sobie plecak, aby użyć plecaka pisz po prostu używam pleceka")
    print("Przed Tobą 4 dzrwi, które wybierasz?")
    choice=input("> ")
    if choice == "1" or "pierwsze":
        redroom()
    elif choice == "2" or "drugie":
        blueroom()
    elif choice == "3" or "trzecie":
        yellowroom()
    elif choice == "4" or "czwarte":
        greenroom()
    else:
        dead("Dobra decyzja! Czas? ...")


start()
