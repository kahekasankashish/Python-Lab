# Q31. Display employee details; calculate DA (30%), HRA (15%), tax (5%), gross/net salary and job tenure.
from datetime import date

name = input("Enter employee name: ")
employee_no = input("Enter employee number: ")
doj_text = input("Enter date of joining (DD/MM/YYYY): ")
department = input("Enter department name: ")
designation = input("Enter designation: ")
basic = float(input("Enter basic salary: "))

day, month, year = map(int, doj_text.split("/"))
doj = date(year, month, day)
today = date.today()
if doj > today:
    print("Date of joining cannot be in the future.")
else:
    da = basic * 0.30
    hra = basic * 0.15
    tax = basic * 0.05
    gross = basic + da + hra
    net = gross - tax

    years = today.year - doj.year
    months = today.month - doj.month
    if today.day < doj.day:
        months -= 1
    if months < 0:
        years -= 1
        months += 12

    print("------ Employee Details ------")
    print("{:<20}: {}".format("Employee Name", name))
    print("{:<20}: {}".format("Employee No", employee_no))
    print("{:<20}: {}".format("Date of Joining", doj_text))
    print("{:<20}: {}".format("Department", department))
    print("{:<20}: {}".format("Designation", designation))
    print("{:<20}: {:.2f}".format("Basic Salary (₹)", basic))
    print("\n------ Salary Details ------")
    print("{:<20}: {:.2f}".format("DA (30%)", da))
    print("{:<20}: {:.2f}".format("HRA (15%)", hra))
    print("{:<20}: {:.2f}".format("Tax (5%)", tax))
    print("{:<20}: {:.2f}".format("Gross Salary (₹)", gross))
    print("{:<20}: {:.2f}".format("Net Salary (₹)", net))
    print("\n------ Job Tenure ------")
    print("Tenure              : {} Years {} Months".format(years, months))
