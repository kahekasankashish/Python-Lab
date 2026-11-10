# Question 10: Input basic salary and compute TA (20%), DA (120%), HRA (30%) and Gross.
basic = float(input("Enter basic salary: "))

ta = 0.20 * basic
da = 1.20 * basic
hra = 0.30 * basic
gross = basic + ta + da + hra

print("TA:", ta)
print("DA:", da)
print("HRA:", hra)
print("Gross salary:", gross)
