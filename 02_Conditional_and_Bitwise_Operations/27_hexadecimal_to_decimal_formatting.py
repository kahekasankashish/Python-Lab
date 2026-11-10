# Q27. Convert a hexadecimal number to decimal using print() output formatting.
value = input("Enter a hexadecimal number: ").strip()
try:
    number = int(value, 16)
    print("Decimal:", format(number, "d"))
except ValueError:
    print("Invalid hexadecimal number.")
