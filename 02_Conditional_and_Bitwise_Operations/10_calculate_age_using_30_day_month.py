# Q10. Calculate age from DOB and current date; assume every month has 30 days.
print("Enter date of birth:")
dd1 = int(input("Day: "))
mm1 = int(input("Month: "))
yy1 = int(input("Year: "))
print("Enter current date:")
dd2 = int(input("Day: "))
mm2 = int(input("Month: "))
yy2 = int(input("Year: "))
if (yy2, mm2, dd2) < (yy1, mm1, dd1):
    print("Current date cannot be earlier than date of birth.")
else:
    if dd2 < dd1:
        dd2 += 30
        mm2 -= 1
    days = dd2 - dd1
    if mm2 < mm1:
        mm2 += 12
        yy2 -= 1
    months = mm2 - mm1
    years = yy2 - yy1
    print(f"Age: {years} years {months} months and {days} days")
