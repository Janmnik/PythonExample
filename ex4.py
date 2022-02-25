#Uważaj na możliwe błędy literowe typu 'plasza'
cars = 100
#Przypisanie zmiennnej przecinkowej przestreni w samochodzie
space_in_a_car = 4.0
#ilość kierowców
drivers = 30
#iloś pasażerów
passengers = 90
#ilość samochodów nie poruszających się
cars_not_driven = cars-drivers
#ilość samochodów poruszających się
cars_driven = drivers
#ilość przetransportowanych osób
carpool_capacity = cars_driven*space_in_a_car
#ilośc średnia umieszczonych osób w samchodzie
average_pasengers_per_car=passengers/cars_driven

print("(Dostępnych jest",cars,"samochodow.")
print("Dostępnych jest tylko",drivers,"kierowców.")
print("Dziś będzie",cars_not_driven,"pustych samochodów.")
print("Dziś możemy przetransportować",carpool_capacity,"osób.")
print("Mamy dziś do przywiezienia",passengers,"pasażerów")
print("Musimy umieścić średnio", average_pasengers_per_car,"osoby w każdym samochodzie.")
