# Q7. Define a function that takes a number as input and returns the number of set bits in it.
def count_set_bits(number):
    if number < 0:
        raise ValueError("Enter a non-negative integer")
    return bin(number).count('1')

number = int(input("Enter a non-negative integer: "))
try:
    print("Number of set bits:", count_set_bits(number))
except ValueError as error:
    print(error)
