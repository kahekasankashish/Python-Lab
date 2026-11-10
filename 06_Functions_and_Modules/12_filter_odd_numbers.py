# Q12. Filter the odd numbers present in a list by using filter().
values = list(map(int, input("Enter integers separated by spaces: ").split()))
odd_values = list(filter(lambda number: number % 2 != 0, values))
print("Odd numbers:", odd_values)
