# Question 9: Print only those numbers present in a list which are divisible by 5.
values = list(map(int, input("Enter list elements separated by spaces: ").split()))
print("Numbers divisible by 5:", [x for x in values if x % 5 == 0])
