# Question 10: Given a list of numbers, return True if the first and last numbers are same.
values = list(map(int, input("Enter list elements separated by spaces: ").split()))
result = len(values) > 0 and values[0] == values[-1]
print(result)
