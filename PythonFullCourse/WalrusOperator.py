# walrus operator: Assigns values to variables as part of an expression
while (input_text := input("Enter text (or 'quit' to exit): ")) != 'quit':
    print("You entered:", input_text)
