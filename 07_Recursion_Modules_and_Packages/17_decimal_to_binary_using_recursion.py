# Q17. Define a recursive function that converts a decimal number to binary.
def decimal_to_binary(number):
    if number < 0:
        return "-" + decimal_to_binary(-number)
    if number < 2:
        return str(number)
    return decimal_to_binary(number // 2) + str(number % 2)

number = int(input("Enter a decimal integer: "))
print("Binary:", decimal_to_binary(number))
