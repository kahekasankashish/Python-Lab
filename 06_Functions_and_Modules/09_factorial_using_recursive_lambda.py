# Q9. Use a recursive lambda function to find the factorial of a number.
factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)

number = int(input("Enter a non-negative integer: "))
if number < 0:
    print("Factorial is not defined for negative integers")
else:
    print("Factorial:", factorial(number))
