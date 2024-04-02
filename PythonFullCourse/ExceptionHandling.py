# exception handling: Mechanism to handle errors gracefully
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Error occurred:", e)
