# Question 3: Find the square root of a number.
import math

number = float(input("Enter a number: "))
if number < 0:
    print("Square root of a negative number is not real.")
else:
    print("Square root:", math.sqrt(number))
