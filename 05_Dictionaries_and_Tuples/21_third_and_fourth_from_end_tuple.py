# Q21. Print the third element from the beginning and the fourth element from the end of a tuple.
items = (10, 20, 30, 40, 50, 60, 70)
if len(items) >= 4:
    print("Third element from beginning:", items[2])
    print("Fourth element from end:", items[-4])
else:
    print("Tuple must contain at least four elements")
