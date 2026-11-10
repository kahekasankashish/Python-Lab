# Question 6: Take two lists and print only their common elements.
first = input("Enter first list elements separated by spaces: ").split()
second = input("Enter second list elements separated by spaces: ").split()
common = []
for item in first:
    if item in second and item not in common:
        common.append(item)
print("Common elements:", common)
