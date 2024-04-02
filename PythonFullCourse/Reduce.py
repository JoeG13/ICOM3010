# reduce: Applies a rolling computation to sequential pairs of values in an iterable
from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print("Product of numbers:", product)
