# higher order functions: Functions that can take other functions as arguments or return functions
def apply_operation(operation, x, y):
    return operation(x, y)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

result_addition = apply_operation(add, 5, 3)
result_subtraction = apply_operation(subtract, 5, 3)

print("Result of addition:", result_addition)
print("Result of subtraction:", result_subtraction)
