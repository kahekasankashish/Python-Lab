# Q25. Remove the elements of a tuple which are present at odd index positions.
items = tuple(input("Enter tuple elements separated by spaces: ").split())
result = items[::2]
print("Tuple after removing odd-index elements:", result)
