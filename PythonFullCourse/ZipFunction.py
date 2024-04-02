# zip function: Combines elements from multiple iterables into tuples
names = ['Joe', 'Alice', 'Bob']
ages = [30, 25, 35]

for name, age in zip(names, ages):
    print(f"Name: {name}, Age: {age}")
