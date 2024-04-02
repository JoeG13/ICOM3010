# **kwargs: Used to pass a variable number of keyword arguments to a function
def greet(**kwargs):
    if 'name' in kwargs:
        print(f"Hello, {kwargs['name']}!")
    else:
        print("Hello, there!")

greet(name="Joe")
