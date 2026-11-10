# Question 15: Split the even and odd elements of a list into two different lists.
values = list(map(int, input("Enter list elements separated by spaces: ").split()))
even = [x for x in values if x % 2 == 0]
odd = [x for x in values if x % 2 != 0]
print("Even elements:", even)
print("Odd elements:", odd)
