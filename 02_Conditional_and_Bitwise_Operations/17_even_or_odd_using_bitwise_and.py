# Q17. Check whether an integer is even or odd using the bitwise AND (&) operator.
number = int(input("Enter an integer: "))
if number & 1:
    print("Odd")
else:
    print("Even")
