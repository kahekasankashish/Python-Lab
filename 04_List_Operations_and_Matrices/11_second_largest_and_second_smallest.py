# Question 11: Find the second largest and second smallest element from a list.
values = list(map(int, input("Enter list elements separated by spaces: ").split()))
unique_values = sorted(set(values))
if len(unique_values) < 2:
    print("At least two distinct values are required.")
else:
    print("Second smallest:", unique_values[1])
    print("Second largest:", unique_values[-2])
