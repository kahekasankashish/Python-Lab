# Q9. Check whether a year is a leap year using the divisibility-by-4, 100 and 400 rules.
year = int(input("Enter a year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
