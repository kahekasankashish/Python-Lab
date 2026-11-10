# Q28. Convert a binary number to decimal using print() output formatting.
value = input("Enter a binary number: ").strip()
try:
    number = int(value, 2)
    print("Decimal:", format(number, "d"))
except ValueError:
    print("Invalid binary number.")
