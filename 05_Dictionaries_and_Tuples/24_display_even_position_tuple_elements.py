# Q24. Display the elements present in a tuple which are at the even position.
items = tuple(input("Enter tuple elements separated by spaces: ").split())
print("Elements at even positions (1-based):", items[1::2])
