# Module EMPLOYEE: salary component functions.
# The assignment does not specify DA, HRA or income-tax rates.
# These functions therefore use clearly stated illustrative rates:
# DA = 10% of basic, HRA = 20% of basic, IT = 5% of gross salary.

def da(basic):
    return 0.10 * basic

def hra(basic):
    return 0.20 * basic

def it(gross):
    return 0.05 * gross
