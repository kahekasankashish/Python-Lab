# Q6. Calculate electricity bill: first 100 units at Rs.1/unit, next 100 at Rs.2/unit, remaining at Rs.3/unit.
previous = float(input("Enter previous meter reading: "))
current = float(input("Enter current meter reading: "))
if current < previous:
    print("Invalid readings: current reading cannot be less than previous reading.")
else:
    units = current - previous
    if units <= 100:
        bill = units * 1
    elif units <= 200:
        bill = 100 * 1 + (units - 100) * 2
    else:
        bill = 100 * 1 + 100 * 2 + (units - 200) * 3
    print("Units consumed:", units)
    print("Total bill: Rs.", bill)
