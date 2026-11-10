# Q19. Check whether a given positive integer is a power of two using bitwise operators.
number = int(input("Enter an integer: "))
if number > 0 and (number & (number - 1)) == 0:
    print(number, "is a power of 2")
else:
    print(number, "is not a power of 2")
