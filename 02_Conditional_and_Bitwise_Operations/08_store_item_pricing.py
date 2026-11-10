# Q8. Calculate total cost: under 10 items Rs.12/item; 10-99 Rs.10/item; 100 or more Rs.7/item.
quantity = int(input("Enter number of items: "))
if quantity < 0:
    print("Quantity cannot be negative.")
elif quantity < 10:
    rate = 12
elif quantity < 100:
    rate = 10
else:
    rate = 7
if quantity >= 0:
    print("Rate per item: Rs.", rate)
    print("Total cost: Rs.", quantity * rate)
