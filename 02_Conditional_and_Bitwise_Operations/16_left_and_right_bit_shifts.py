# Q16. Perform left shift (<<) and right shift (>>) operations on an integer and display the results.
number = int(input("Enter an integer: "))
positions = int(input("Enter number of positions to shift: "))
if positions < 0:
    print("Number of shift positions cannot be negative.")
else:
    print("Left shift:", number << positions)
    print("Right shift:", number >> positions)
    print("Left shift by n multiplies by 2**n; right shift by n performs integer division by 2**n for non-negative numbers.")
