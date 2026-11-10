# Q18. Define a function named binary_search that takes a list and an item to search for, and returns the index where the item is available.
def binary_search(values, item):
    low, high = 0, len(values) - 1
    while low <= high:
        middle = (low + high) // 2
        if values[middle] == item:
            return middle
        if item < values[middle]:
            high = middle - 1
        else:
            low = middle + 1
    return -1

numbers = list(map(int, input("Enter sorted integers separated by spaces: ").split()))
item = int(input("Enter item to search: "))
print("Index:", binary_search(numbers, item))
