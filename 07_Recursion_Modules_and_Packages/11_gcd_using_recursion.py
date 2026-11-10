# Q11. Define a recursive function that returns the GCD of two numbers.
def gcd(a, b):
    if b == 0:
        return abs(a)
    return gcd(b, a % b)

a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
print("GCD:", gcd(a, b))
