# Q1. Define an Employee class with empName, empID and empBasicSal, constructors and necessary member functions. Define Manager inherited from Employee with a bonus data member. Create a Manager object and access its details.
class Employee:
    def __init__(self, empName, empID, empBasicSal):
        self.empName = empName
        self.empID = empID
        self.empBasicSal = empBasicSal

    def display(self):
        print("Employee Name:", self.empName)
        print("Employee ID:", self.empID)
        print("Employee basic salary:", self.empBasicSal)


class Manager(Employee):
    def __init__(self, empName, empID, empBasicSal, bonus):
        super().__init__(empName, empID, empBasicSal)
        self.bonus = bonus

    def display(self):
        super().display()
        print("Bonus:", self.bonus)
        print("Total salary:", self.empBasicSal + self.bonus)


manager = Manager("Kashish Kahekasan", 2754, 78000, 10000)
manager.display()
