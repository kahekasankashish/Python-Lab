# Q7. Calculate income tax: up to Rs.2,50,000 no tax; next Rs.2,50,000 at 5%; amount above Rs.5,00,000 at 10%.
income = float(input("Enter annual income: "))
if income < 0:
    print("Income cannot be negative.")
else:
    if income <= 250000:
        tax = 0
    elif income <= 500000:
        tax = (income - 250000) * 0.05
    else:
        tax = 250000 * 0.05 + (income - 500000) * 0.10
    # Progressive slab calculation, following the notebook's intended structure.
    print("Income tax payable: Rs.", tax)
