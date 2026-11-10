# Q8. Define an Employee class with empName, empNumber, basicSal, DA and HRA; implement calGrossSal() and showEmpDetails(). Create employee objects and display employees whose gross salary exceeds 50,000.
class Employee:
    def __init__(self, empName, empNumber, basicSal, da_rate=0.20, hra_rate=0.50):
        self.empName = empName
        self.empNumber = empNumber
        self.basicSal = float(basicSal)
        # Rates follow the example in the supplied solution screenshot.
        self.DA = da_rate * self.basicSal
        self.HRA = hra_rate * self.basicSal

    def calGrossSal(self):
        return self.basicSal + self.DA + self.HRA

    def showEmpDetails(self):
        print(f"Employee name: {self.empName}")
        print(f"Employee number: {self.empNumber}")
        print(f"Basic salary: {self.basicSal:.2f}")
        print(f"DA: {self.DA:.2f}")
        print(f"HRA: {self.HRA:.2f}")
        print(f"Gross salary: {self.calGrossSal():.2f}")

employees = []
count = int(input("Enter number of employees: "))
for index in range(count):
    print(f"\nEnter details for employee {index + 1}:")
    name = input("Employee name: ").strip()
    number = input("Employee number: ").strip()
    salary = float(input("Basic salary: "))
    employees.append(Employee(name, number, salary))

print("\nEmployees with gross salary greater than 50,000:")
found = False
for employee in employees:
    if employee.calGrossSal() > 50000:
        employee.showEmpDetails()
        print("-" * 30)
        found = True
if not found:
    print("No employee has a gross salary greater than 50,000.")
