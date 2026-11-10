# Question 17: Enter coordinates of two points of a square and calculate its area and perimeter.
import math

x1 = float(input("Enter x-coordinate of first point: "))
y1 = float(input("Enter y-coordinate of first point: "))
x2 = float(input("Enter x-coordinate of second point: "))
y2 = float(input("Enter y-coordinate of second point: "))

# The question's example treats the distance between the entered points as the side.
side = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
area = side ** 2
perimeter = 4 * side

print("Side of the square:", side)
print("Area:", area)
print("Perimeter:", perimeter)
