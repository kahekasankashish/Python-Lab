# Q1. Define a class Point for two-dimensional points. Create three Point objects and check whether the points are non-collinear.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def are_non_collinear(p1, p2, p3):
        # Twice the signed area of the triangle; non-zero means non-collinear.
        area_twice = (
            p1.x * (p2.y - p3.y)
            + p2.x * (p3.y - p1.y)
            + p3.x * (p1.y - p2.y)
        )
        return area_twice != 0

p1 = Point(1, 2)
p2 = Point(5, 2)
p3 = Point(9, 5)
if Point.are_non_collinear(p1, p2, p3):
    print("Points are not collinear.")
else:
    print("Points are collinear.")
