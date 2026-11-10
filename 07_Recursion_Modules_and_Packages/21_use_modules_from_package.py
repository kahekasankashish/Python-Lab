# Q21. Create a package containing different modules and use the functionality of the modules defined inside the package.
from utility_package import arithmetic, geometry

print("Addition:", arithmetic.add(10, 5))
print("Multiplication:", arithmetic.multiply(10, 5))
print("Circle area (radius 3):", geometry.circle_area(3))
print("Rectangle area (4 x 6):", geometry.rectangle_area(4, 6))
