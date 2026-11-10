# Q14. Store students' roll numbers and names in a dictionary; display all records, add a record, delete a record, and modify an existing student's name.
students = {}
count = int(input("How many students do you want to enter? "))
for _ in range(count):
    roll = input("Enter roll number: ").strip()
    name = input("Enter student name: ").strip()
    students[roll] = name

print("\nStudent records:")
for roll, name in students.items():
    print(roll, ":", name)

new_roll = input("\nEnter new roll number: ").strip()
new_name = input("Enter new student name: ").strip()
students[new_roll] = new_name
print("After adding:", students)

delete_roll = input("Enter roll number to delete: ").strip()
if delete_roll in students:
    del students[delete_roll]
else:
    print("Roll number not found")

modify_roll = input("Enter roll number whose name you want to modify: ").strip()
if modify_roll in students:
    students[modify_roll] = input("Enter corrected name: ").strip()
else:
    print("Roll number not found")
print("Final student dictionary:", students)
