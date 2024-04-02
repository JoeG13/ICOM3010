# nested function calls: Calling a function within another function
def outer_function():
    def inner_function():
        print("Inside inner function")

    print("Inside outer function")
    inner_function()


outer_function()
