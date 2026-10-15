#Jest, ma, obiekty i klasy
##Animal jest obiektem (tak trochę dezoriontujące)
class Animal(object):
    pass
##Dog ma relację 
class Dog(Animal):
    def __init__(self, name):
        #przypisanie wartości przekazaną jako argument name do atrybutu name obiektu
        self.name = name
##Cat jest obiektem
class Cat(Animal):
    def __init__(self, name):
        ##przypisanie wartości przekazaną jako argument do atrybutu name obiektu
        self.name = name

##Person jest obiektem
class Person(object):
    def __init__(self, name):
        ##przypisanie  wartości przekazaną jako agument do atrybutu name obiektu
        self.name = name
        
        ## Person ma pet
        self.pet = None
##Person
class Employee(Person):
    def __init__(self, name, salary):
        ##dziwna magia, super dziedziczy
        super(Employee, self).__init__(name)
        ##
        self.salary = salary

##
class Fish(object):
    pass
##
class Salmon(Fish):
    pass
##
class Halibut(Fish):
    pass

##rover jest Dog (psem)
rover = Dog("Rover")
##
satan = Cat("Satan")

##
mary.pet = satan

##
frank = Eployee("Frank", 12000)

##
frank.pet = rover

##
flipper = Fish()

##
crouse = Salmon()

##
harry = Halibut()
















