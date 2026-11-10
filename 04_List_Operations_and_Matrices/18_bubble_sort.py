# Question 18: Sort elements in a list using bubble sort.
values = list(map(int, input("Enter list elements separated by spaces: ").split()))
for i in range(len(values)):
    swapped = False
    for j in range(0, len(values) - i - 1):
        if values[j] > values[j + 1]:
            values[j], values[j + 1] = values[j + 1], values[j]
            swapped = True
    if not swapped:
        break
print("Sorted list:", values)
