# Q21. Check whether a number contains a pair of adjacent set bits in its binary representation.
number = int(input("Enter a non-negative integer: "))
if number < 0:
    print("Please enter a non-negative integer.")
elif number & (number >> 1):
    print("Yes, there is a pair of adjacent set bits.")
else:
    print("No adjacent set bits were found.")
