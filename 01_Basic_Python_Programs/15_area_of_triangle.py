# Question 15: Input three sides of a triangle and print its area.
import math

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if a + b > c and a + c > b and b + c > a:
    semi_perimeter = (a + b + c) / 2
    area = math.sqrt(semi_perimeter * (semi_perimeter - a) *
                     (semi_perimeter - b) * (semi_perimeter - c))
    print("Area of triangle:", area)
else:
    print("The entered sides do not form a valid triangle.")
