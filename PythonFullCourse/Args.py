# *args: Used to pass a variable number of arguments to a function
def greet(*args):
    if args:
        for name in args:
            print(f"Hello, {name}!")
    else:
        print("Hello, there!")

greet("Joe", "Emily", "Bob")
