# Q13. Write a program to calculate the power of a number using recursion.
def power(base, exponent):
    if exponent < 0:
        if base == 0:
            raise ZeroDivisionError("Zero cannot have a negative exponent")
        return 1 / power(base, -exponent)
    if exponent == 0:
        return 1
    if exponent % 2 == 0:
        half = power(base, exponent // 2)
        return half * half
    return base * power(base, exponent - 1)

base = float(input("Enter base: "))
exponent = int(input("Enter integer exponent: "))
try:
    print("Result:", power(base, exponent))
except ZeroDivisionError as error:
    print(error)
