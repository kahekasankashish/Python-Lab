# Q20. Toggle (flip) the k-th bit of an integer (bit positions are counted from 0 at the right).
number = int(input("Enter an integer: "))
k = int(input("Enter bit position k: "))
if k < 0:
    print("Bit position cannot be negative.")
else:
    toggled = number ^ (1 << k)
    print("After toggling:", toggled)
