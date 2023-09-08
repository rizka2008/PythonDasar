class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")
class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model 

    def move(self):
        print("Sail!")
class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model 

    def move(self):
        print("Fly!")
car1 = Car("Ford", "Mustang") #Create a Car class
boat1 = Boat("lbiza", "Touring 20") #Create a Boat class
Plane1 = Plane("Boeing", "747") #Create a Plane class

for x in (car1, boat1, Plane1):
    x.move()
