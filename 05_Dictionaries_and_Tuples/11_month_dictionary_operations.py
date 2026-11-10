# Q11. Create a dictionary of month names and number of days; ask for a month, print its days, print keys alphabetically, and print all months with 31 days.
months = {
    'jan': 31, 'feb': 28, 'mar': 31, 'apr': 30,
    'may': 31, 'jun': 30, 'jul': 31, 'aug': 31,
    'sep': 30, 'oct': 31, 'nov': 30, 'dec': 31
}
month = input("Enter month name (full name or 3-letter abbreviation): ").strip().lower()
month = month[:3]
if month in months:
    print("Number of days:", months[month])
else:
    print("Invalid month")
print("\nMonths in alphabetical order:")
for name in sorted(months):
    print(name)
print("\nMonths with 31 days:")
for name, days in months.items():
    if days == 31:
        print(name)
