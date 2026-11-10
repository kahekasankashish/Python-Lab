# Q11. Find the reverse of a number using recursion.
def reverse_number(number, reversed_number=0):
    if number == 0:
        return reversed_number
    return reverse_number(number // 10, reversed_number * 10 + number % 10)

number = int(input("Enter a non-negative integer: "))
if number < 0:
    print("Please enter a non-negative integer")
else:
    print("Reversed number:", reverse_number(number))
