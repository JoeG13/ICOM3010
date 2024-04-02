# inheritance: Mechanism for creating new classes that derive properties and behavior from existing ones
class Animal:
    def sound(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

dog = Dog()
dog.sound()  # Output: Animal speaks
dog.bark()  # Output: Dog barks
