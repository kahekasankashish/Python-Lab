# Question 4: Print all the elements in a list that are greater than a given value.
values = list(map(int, input("Enter list elements separated by spaces: ").split()))
limit = int(input("Enter the comparison value: "))
print("Elements greater than", limit, ":", [x for x in values if x > limit])
