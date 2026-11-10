# Q15. Write a recursive function that performs binary search.
def recursive_binary_search(values, target, low, high):
    if low > high:
        return -1
    middle = (low + high) // 2
    if values[middle] == target:
        return middle
    if target < values[middle]:
        return recursive_binary_search(values, target, low, middle - 1)
    return recursive_binary_search(values, target, middle + 1, high)

numbers = list(map(int, input("Enter sorted integers separated by spaces: ").split()))
target = int(input("Enter value to search: "))
print("Index:", recursive_binary_search(numbers, target, 0, len(numbers) - 1))
