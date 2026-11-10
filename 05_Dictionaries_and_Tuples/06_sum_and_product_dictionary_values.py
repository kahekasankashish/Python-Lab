# Q6. Print the sum and product of all the values present in a dictionary.
values = {'a': 2, 'b': 3, 'c': 4}
total = sum(values.values())
product = 1
for value in values.values():
    product *= value
print("Sum:", total)
print("Product:", product)
