# multilevel inheritance: Inheritance where a derived class inherits from another derived class
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Labrador(Dog):
    def color(self):
        print("Labrador is brown")

labrador = Labrador()
labrador.sound()  # Output: Animal makes a sound
labrador.bark()   # Output: Dog barks
labrador.color()  # Output: Labrador is brown
