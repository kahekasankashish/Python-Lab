"""
Question: Write a program that takes two numbers as input and computes their Least Common Multiple (LCM).
"""

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
x, y = abs(a), abs(b)
p, q = x, y

while q:
    p, q = q, p % q

gcd = p
lcm = 0 if x == 0 or y == 0 else (x * y) // gcd
print("LCM:", lcm)
