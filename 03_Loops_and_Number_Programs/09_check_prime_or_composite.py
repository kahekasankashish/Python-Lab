"""
Question: Write a program to check whether a given number is prime or composite.
"""

number = int(input("Enter an integer: "))

if number <= 1:
    print(number, "is neither prime nor composite.")
else:
    is_prime = True
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            is_prime = False
            break
    if is_prime:
        print(number, "is prime.")
    else:
        print(number, "is composite.")
