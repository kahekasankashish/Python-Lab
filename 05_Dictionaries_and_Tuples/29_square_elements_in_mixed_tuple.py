# Q29. Take a tuple of mixed data types and find the square of each numeric element.
items = (2, 3.5, 'Python', 4, True)
squares = tuple(value ** 2 if isinstance(value, (int, float)) and not isinstance(value, bool) else value for value in items)
print("Original tuple:", items)
print("Result:", squares)
