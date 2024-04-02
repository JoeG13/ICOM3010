# duck typing: Principle in dynamic typing where the object's suitability for a task is determined by its methods and properties
class Dog:
    def sound(self):
        return "Woof"

class Cat:
    def sound(self):
        return "Meow"

def make_sound(animal):
    print(animal.sound())

make_sound(Dog())  # Output: Woof
make_sound(Cat())  # Output: Meow
