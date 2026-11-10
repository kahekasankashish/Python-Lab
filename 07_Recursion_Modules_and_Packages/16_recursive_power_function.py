# Q16. Define a recursive function to compute power(a, b).
def power(a, b):
    if b < 0:
        if a == 0:
            raise ZeroDivisionError("Zero cannot have a negative exponent")
        return 1 / power(a, -b)
    if b == 0:
        return 1
    if b % 2 == 0:
        half = power(a, b // 2)
        return half * half
    return a * power(a, b - 1)

base = float(input("Enter a: "))
exponent = int(input("Enter b (integer): "))
try:
    print("a raised to b:", power(base, exponent))
except ZeroDivisionError as error:
    print(error)
