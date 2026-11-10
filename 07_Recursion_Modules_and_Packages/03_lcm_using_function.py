# Q3. Define a function that takes two numbers as parameters and returns their LCM.
def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    x, y = abs(a), abs(b)
    while y:
        x, y = y, x % y
    return abs(a * b) // x

first = int(input("Enter first integer: "))
second = int(input("Enter second integer: "))
print("LCM:", lcm(first, second))
