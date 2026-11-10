# Q31. Print only those elements present in a tuple which are divisible by 5.
items = (10, 12, 15, 22, 25, 31, 40)
print("Elements divisible by 5:", tuple(number for number in items if number % 5 == 0))
