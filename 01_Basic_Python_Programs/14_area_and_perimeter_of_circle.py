# Question 14: Input the radius of a circle and print its area and perimeter.
import math

radius = float(input("Enter radius: "))
area = math.pi * radius ** 2
perimeter = 2 * math.pi * radius

print("Area:", area)
print("Perimeter:", perimeter)
