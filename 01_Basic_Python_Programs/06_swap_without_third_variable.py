# Question 6: Swap the values of two variables without using a third variable.
a = input("Enter the first value: ")
b = input("Enter the second value: ")

a, b = b, a

print("Values after swapping:")
print("a =", a)
print("b =", b)
