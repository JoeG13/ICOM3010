# Object Oriented Programming (OOP): Creating classes and objects to model real-world entities
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car: {self.year} {self.make} {self.model}")

my_car = Car("Toyota", "Camry", 2020)
my_car.display_info()
