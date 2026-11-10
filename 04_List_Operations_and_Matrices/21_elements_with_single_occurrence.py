# Question 21: Print all elements in a list that have only a single occurrence.
values = list(map(int, input("Enter list elements separated by spaces: ").split()))
print("Elements occurring once:", [x for x in values if values.count(x) == 1])
