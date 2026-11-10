# Question 7: Enter a three-digit number and compute its reverse.
number = int(input("Enter a three-digit number: "))
sign = -1 if number < 0 else 1
number = abs(number)

reverse = 0
while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number //= 10

print("Reverse:", sign * reverse)
