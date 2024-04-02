# method chaining: Invoking multiple methods of an object in a single line
class Calculator:
    def __init__(self, x):
        self.x = x

    def add(self, y):
        self.x += y
        return self

    def multiply(self, y):
        self.x *= y
        return self

result = Calculator(5).add(3).multiply(2).x
print("Result:", result)
