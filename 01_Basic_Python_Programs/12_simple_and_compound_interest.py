# Question 12: Input amount and compute simple interest and compound interest.
principal = float(input("Enter principal amount: "))
rate = float(input("Enter annual rate of interest (%): "))
time = float(input("Enter time period in years: "))

simple_interest = (principal * rate * time) / 100
compound_interest = principal * ((1 + rate / 100) ** time) - principal

print("Simple interest:", simple_interest)
print("Compound interest:", compound_interest)
