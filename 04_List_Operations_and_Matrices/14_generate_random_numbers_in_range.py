# Question 14: Generate random numbers within a given range and store them in a list.
import random
lower = int(input("Enter lower limit: "))
upper = int(input("Enter upper limit: "))
count = int(input("How many random numbers? "))
if lower > upper or count < 0:
    print("Invalid range or count.")
else:
    numbers = [random.randint(lower, upper) for _ in range(count)]
    print("Random numbers:", numbers)
