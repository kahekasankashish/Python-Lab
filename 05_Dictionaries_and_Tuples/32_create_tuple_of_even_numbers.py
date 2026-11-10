# Q32. Given a tuple of numbers, create another tuple containing only the even numbers.
numbers = tuple(map(int, input("Enter numbers separated by spaces: ").split()))
even_numbers = tuple(number for number in numbers if number % 2 == 0)
print("Even numbers tuple:", even_numbers)
