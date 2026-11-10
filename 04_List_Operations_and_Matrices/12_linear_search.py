# Question 12: Search an element present in a list using linear search.
values = list(map(int, input("Enter list elements separated by spaces: ").split()))
target = int(input("Enter element to search: "))
for index, value in enumerate(values):
    if value == target:
        print("Element found at position:", index)
        break
else:
    print("Element not found.")
