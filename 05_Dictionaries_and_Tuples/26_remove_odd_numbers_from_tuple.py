# Q26. Remove the odd-number elements from a tuple.
items = (1, 2, 3, 4, 5, 6, 7, 8)
result = tuple(number for number in items if number % 2 == 0)
print("Tuple after removing odd numbers:", result)
