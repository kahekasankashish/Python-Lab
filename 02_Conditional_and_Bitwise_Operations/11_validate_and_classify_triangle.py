# Q11. Validate a triangle from three sides and classify it as isosceles, scalene, equilateral or right-angled.
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))
if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
    print("Invalid triangle")
else:
    if a == b == c:
        print("Equilateral triangle")
    elif a == b or b == c or a == c:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")
    x, y, z = sorted((a, b, c))
    if abs(x*x + y*y - z*z) < 1e-9:
        print("Right-angled triangle")
