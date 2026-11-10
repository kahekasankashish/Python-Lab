# Question 20: Merge two lists into a sorted list.
first = list(map(int, input("Enter first list elements separated by spaces: ").split()))
second = list(map(int, input("Enter second list elements separated by spaces: ").split()))
merged = sorted(first + second)
print("Merged sorted list:", merged)
