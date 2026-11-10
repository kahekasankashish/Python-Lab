# Question 3: Find the position of maximum and minimum element in a list.
values = list(map(int, input("Enter list elements separated by spaces: ").split()))
if not values:
    print("The list is empty.")
else:
    maximum, minimum = max(values), min(values)
    print("Maximum element:", maximum, "Position(s):", [i for i, x in enumerate(values) if x == maximum])
    print("Minimum element:", minimum, "Position(s):", [i for i, x in enumerate(values) if x == minimum])
