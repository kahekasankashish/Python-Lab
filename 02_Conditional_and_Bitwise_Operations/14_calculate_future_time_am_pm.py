# Q14. Given an hour (1-12), am/pm and hours ahead, display the future time.
hour = int(input("Enter hour (1-12): "))
period = input("Enter am or pm: ").strip().lower()
hours_ahead = int(input("How many hours ahead? "))
if not 1 <= hour <= 12 or period not in ("am", "pm") or hours_ahead < 0:
    print("Invalid input.")
else:
    current = hour % 12 + (12 if period == "pm" else 0)
    future = (current + hours_ahead) % 24
    new_hour = future % 12
    if new_hour == 0:
        new_hour = 12
    new_period = "am" if future < 12 else "pm"
    print(f"New time: {new_hour} {new_period}")
