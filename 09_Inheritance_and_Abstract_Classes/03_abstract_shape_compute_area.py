# Q3. Define an abstract class Shape with data members dimOne and dimTwo. Extend it to concrete classes Rectangle and Triangle. Override computeArea() in the subclasses, create derived-class objects and invoke computeArea().
from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, dimOne, dimTwo):
        self.dimOne = dimOne
        self.dimTwo = dimTwo

    @abstractmethod
    def computeArea(self):
        pass


class Rectangle(Shape):
    def computeArea(self):
        return self.dimOne * self.dimTwo


class Triangle(Shape):
    def computeArea(self):
        return 0.5 * self.dimOne * self.dimTwo


rectangle = Rectangle(10, 5)
triangle = Triangle(10, 5)

print("Area of rectangle:", rectangle.computeArea())
print("Area of triangle:", triangle.computeArea())
