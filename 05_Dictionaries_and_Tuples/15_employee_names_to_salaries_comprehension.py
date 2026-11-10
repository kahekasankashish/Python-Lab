# Q15. Given an employee-ID-to-salary dictionary and a list of employee names, write a comprehension mapping employee names to salaries.
id2salary = {0: 1000.0, 3: 990, 1: 1200.50}
names = ['Larry', 'Curly', 'Moe']
name2salary = {names[employee_id]: salary for employee_id, salary in id2salary.items() if employee_id < len(names)}
print(name2salary)
