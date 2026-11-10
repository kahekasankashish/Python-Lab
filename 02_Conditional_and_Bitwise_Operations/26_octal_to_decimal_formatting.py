# Q26. Convert an octal number to decimal using print() output formatting.
value = input("Enter an octal number: ").strip()
try:
    number = int(value, 8)
    print("Decimal:", format(number, "d"))
except ValueError:
    print("Invalid octal number.")
