# Q9. Create a nested dictionary for three employees with ID, name and designation; add a fourth employee with salary; display old and new dictionaries; remove the third employee and display the collection.
employees = {
    1: {'id': 101, 'name': 'Amit', 'designation': 'Manager'},
    2: {'id': 102, 'name': 'Neha', 'designation': 'Developer'},
    3: {'id': 103, 'name': 'Ravi', 'designation': 'Analyst'}
}
print("Original employee dictionary:")
print(employees)

employees[4] = {'id': 104, 'name': 'Priya', 'designation': 'Designer', 'salary': 45000}
print("\nAfter adding the fourth employee:")
print(employees)

del employees[3]
print("\nAfter removing the third employee:")
print(employees)
