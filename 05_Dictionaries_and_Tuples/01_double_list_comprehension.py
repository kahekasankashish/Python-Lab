# Q1. Write a double list comprehension over ['A','B','C'] and [1,2,3] whose value is the list of all possible two-element lists [letter, number].
letters = ['A', 'B', 'C']
numbers = [1, 2, 3]
result = [[letter, number] for letter in letters for number in numbers]
print(result)
