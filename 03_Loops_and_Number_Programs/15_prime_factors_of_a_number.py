"""
Question: Write a program to find and display the prime factors of a given number.
"""

number = int(input("Enter an integer greater than 1: "))

if number <= 1:
    print("Prime factors are defined here for integers greater than 1.")
else:
    print("Prime factors:")
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            print(divisor)
            while number % divisor == 0:
                number //= divisor
        divisor += 1
    if number > 1:
        print(number)
