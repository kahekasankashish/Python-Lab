# Question 13: Search an element of a list using binary search.
values = list(map(int, input("Enter sorted list elements separated by spaces: ").split()))
target = int(input("Enter element to search: "))
low, high = 0, len(values) - 1
found = -1
while low <= high:
    mid = (low + high) // 2
    if values[mid] == target:
        found = mid
        break
    if values[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
if found >= 0:
    print("Element found at position:", found)
else:
    print("Element not found.")
