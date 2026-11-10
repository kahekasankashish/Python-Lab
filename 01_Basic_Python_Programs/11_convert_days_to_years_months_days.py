# Question 11: Convert total days into years, months and remaining days (1 year = 365 days, 1 month = 30 days).
total_days = int(input("Enter total number of days: "))

years = total_days // 365
remaining_days = total_days % 365
months = remaining_days // 30
days = remaining_days % 30

print(f"{years} year(s), {months} month(s), {days} day(s)")
