# Q12. Convert a non-negative length in centimetres to inches (1 inch = 2.54 cm).
cm = float(input("Enter length in centimetres: "))
if cm < 0:
    print("Invalid entry: length cannot be negative.")
else:
    inches = cm / 2.54
    print("Length in inches:", inches)
