# variable scope: The region where a variable is accessible
def my_function():
    x = 10  # Local variable
    print("Inside function, x =", x)

x = 5  # Global variable
my_function()
print("Outside function, x =", x)
