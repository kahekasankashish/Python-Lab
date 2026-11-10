# Question 17: Using list comprehension: (a) print even numbers within 20,
# (b) display squares of numbers from 0 to 10, and (c) show the first letter of each word.
even_numbers = [n for n in range(21) if n % 2 == 0]
squares = [n ** 2 for n in range(11)]
words = input("Enter words separated by spaces: ").split()
first_letters = [word[0] for word in words if word]
print("Even numbers within 20:", even_numbers)
print("Squares from 0 to 10:", squares)
print("First letters:", first_letters)
