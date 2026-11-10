# Q14. Find the area of a circle, square, triangle and rectangle by using different functions and group them in a module SHAPES.
import SHAPES

radius = float(input("Enter circle radius: "))
side = float(input("Enter square side: "))
base = float(input("Enter triangle base: "))
height = float(input("Enter triangle height: "))
length = float(input("Enter rectangle length: "))
width = float(input("Enter rectangle width: "))

print("Circle area:", SHAPES.circle_area(radius))
print("Square area:", SHAPES.square_area(side))
print("Triangle area:", SHAPES.triangle_area(base, height))
print("Rectangle area:", SHAPES.rectangle_area(length, width))
