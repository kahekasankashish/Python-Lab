# Question 2: Find the maximum and minimum element of a list.
values = list(map(int, input("Enter list elements separated by spaces: ").split()))
if not values:
    print("The list is empty.")
else:
    print("Maximum:", max(values))
    print("Minimum:", min(values))
