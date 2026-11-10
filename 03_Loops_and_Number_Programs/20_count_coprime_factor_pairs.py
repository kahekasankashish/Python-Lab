"""
Question: Given a number N, write a program to determine the number of coprime pairs (a, b) such that 1 <= a, b <= N, a*b = N, and gcd(a, b) = 1.
"""

n = int(input("Enter a positive integer N: "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    count = 0
    pairs = []
    for a in range(1, n + 1):
        if n % a == 0:
            b = n // a
            x, y = a, b
            while y:
                x, y = y, x % y
            if x == 1:
                count += 1
                pairs.append((a, b))
    print("Coprime factor pairs:", pairs)
    print("Number of coprime pairs:", count)
