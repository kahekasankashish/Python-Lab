"""
Question: Write a program to find all numbers less than a given number N that are coprime with N.
"""

n = int(input("Enter a positive integer N: "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    print(f"Numbers less than {n} that are coprime with it:")
    for number in range(1, n):
        a, b = number, n
        while b:
            a, b = b, a % b
        if a == 1:
            print(number)
