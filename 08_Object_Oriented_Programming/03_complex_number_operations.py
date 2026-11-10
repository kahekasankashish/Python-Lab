# Q3. Define a class ComplexNumber with necessary data members and member functions to perform basic complex-number operations.
class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other):
        real = self.real * other.real - self.imaginary * other.imaginary
        imaginary = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(real, imaginary)

    def __truediv__(self, other):
        denominator = other.real ** 2 + other.imaginary ** 2
        if denominator == 0:
            raise ZeroDivisionError("Cannot divide by zero complex number")
        real = (self.real * other.real + self.imaginary * other.imaginary) / denominator
        imaginary = (self.imaginary * other.real - self.real * other.imaginary) / denominator
        return ComplexNumber(real, imaginary)

    def __str__(self):
        sign = "+" if self.imaginary >= 0 else "-"
        return f"{self.real} {sign} {abs(self.imaginary)}i"

first = ComplexNumber(5, 3)
second = ComplexNumber(2, 2)
print("Addition:", first + second)
print("Subtraction:", first - second)
print("Multiplication:", first * second)
try:
    print("Division:", first / second)
except ZeroDivisionError as error:
    print(error)
