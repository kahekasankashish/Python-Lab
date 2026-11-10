# Question 19: Sort elements in a list using insertion sort.
values = list(map(int, input("Enter list elements separated by spaces: ").split()))
for i in range(1, len(values)):
    key = values[i]
    j = i - 1
    while j >= 0 and values[j] > key:
        values[j + 1] = values[j]
        j -= 1
    values[j + 1] = key
print("Sorted list:", values)
