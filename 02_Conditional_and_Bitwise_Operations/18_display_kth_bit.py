# Q18. Display the k-th bit of a given integer (bit positions are counted from 0 at the right).
number = int(input("Enter an integer: "))
k = int(input("Enter bit position k: "))
if k < 0:
    print("Bit position cannot be negative.")
else:
    bit = (number >> k) & 1
    print("The k-th bit is:", bit)
