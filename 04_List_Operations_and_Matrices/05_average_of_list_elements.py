# Question 5: Find the average of all elements present in a list.
values = list(map(float, input("Enter list elements separated by spaces: ").split()))
if values:
    print("Average:", sum(values) / len(values))
else:
    print("The list is empty; average is undefined.")
