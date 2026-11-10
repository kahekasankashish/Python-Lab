# Q27. Reverse the elements of a tuple by using and without using a built-in function.
items = (10, 20, 30, 40, 50)
print("Using built-in reversed():", tuple(reversed(items)))
print("Without reversed() (slicing):", items[::-1])
