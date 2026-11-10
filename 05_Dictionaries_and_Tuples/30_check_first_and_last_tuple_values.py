# Q30. Given a tuple of numbers, return True if the first and last numbers are the same.
numbers = tuple(map(int, input("Enter numbers separated by spaces: ").split()))
result = len(numbers) > 0 and numbers[0] == numbers[-1]
print(result)
