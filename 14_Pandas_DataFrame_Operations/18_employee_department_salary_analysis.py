# Q18. Create a DataFrame with EmpID, Name, Department and Salary. Display employees in a user-specified department, increase all salaries by 10%, find highest and lowest salary, group by department for average salary, and save the DataFrame to CSV.
import pandas as pd

employees = pd.DataFrame({
    "EmpID": [1, 2, 3, 4, 5, 6],
    "Name": ["Asha", "Rahul", "Neha", "Karan", "Isha", "Dev"],
    "Department": ["HR", "IT", "Finance", "IT", "HR", "Finance"],
    "Salary": [35000, 55000, 48000, 62000, 39000, 51000]
})

department = input("Enter department to display: ").strip()
print("\nEmployees in", department, ":")
print(employees[employees["Department"].str.casefold() == department.casefold()])

employees["Salary"] = employees["Salary"] * 1.10
print("\nAfter 10% salary increment:")
print(employees)

print("\nHighest salary:", employees["Salary"].max())
print("Lowest salary:", employees["Salary"].min())

print("\nAverage salary by department:")
print(employees.groupby("Department")["Salary"].mean())

employees.to_csv("employee_salary.csv", index=False)
print("\nDataFrame saved to employee_salary.csv")
