# Q15. Create separate functions for calculating DA, HRA and IT of an employee within a module EMPLOYEE. Use da(), hra() and it() for calculating GROSS and NET salary. GROSS = BASIC + DA + HRA and NET_SALARY = GROSS - TAX.
import EMPLOYEE

basic = float(input("Enter basic salary: "))
da_amount = EMPLOYEE.da(basic)
hra_amount = EMPLOYEE.hra(basic)
tax = EMPLOYEE.it(basic + da_amount + hra_amount)
gross = basic + da_amount + hra_amount
net_salary = gross - tax

print(f"Basic salary: {basic:.2f}")
print(f"DA: {da_amount:.2f}")
print(f"HRA: {hra_amount:.2f}")
print(f"Gross salary: {gross:.2f}")
print(f"Income tax: {tax:.2f}")
print(f"Net salary: {net_salary:.2f}")
