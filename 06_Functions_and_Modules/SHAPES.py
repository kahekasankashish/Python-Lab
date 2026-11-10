# Module SHAPES: area functions for circle, square, triangle and rectangle.
import math

def circle_area(radius):
    return math.pi * radius ** 2

def square_area(side):
    return side ** 2

def triangle_area(base, height):
    return 0.5 * base * height

def rectangle_area(length, width):
    return length * width
