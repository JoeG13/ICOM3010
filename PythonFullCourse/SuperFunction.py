# super function: Calling a method from the parent class
class Parent:
    def show(self):
        print("Parent class method")

class Child(Parent):
    def show(self):
        super().show()  # Calling parent class method
        print("Child class method")

child = Child()
child.show()
