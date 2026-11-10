# Q19. Create a student DataFrame with roll No, name, marks and city. Select rows where marks > 80, filter by a specific city, select columns using loc[] and iloc[], update a student's marks, and delete a column.
import pandas as pd

student = pd.DataFrame({
    "roll No": [1, 2, 3, 4, 5],
    "name": ["Aman", "Riya", "Sahil", "Tina", "Vivek"],
    "marks": [85, 72, 91, 68, 88],
    "city": ["Bhubaneswar", "Cuttack", "Bhubaneswar", "Puri", "Cuttack"]
})

print("Students with marks greater than 80:")
print(student[student["marks"] > 80])

city = input("\nEnter city to filter: ").strip()
print(student[student["city"].str.casefold() == city.casefold()])

print("\nUsing loc[] (rows 0-2, name and marks):")
print(student.loc[0:2, ["name", "marks"]])

print("\nUsing iloc[] (first three rows, first two columns):")
print(student.iloc[0:3, 0:2])

roll_number = int(input("\nEnter roll number whose marks should be updated: "))
new_marks = float(input("Enter updated marks: "))
if student["roll No"].eq(roll_number).any():
    student.loc[student["roll No"] == roll_number, "marks"] = new_marks
    print("Marks updated.")
else:
    print("Roll number not found.")

column_to_delete = input("Enter column name to delete (roll No/name/marks/city): ").strip()
if column_to_delete in student.columns:
    student = student.drop(columns=[column_to_delete])
    print("Updated DataFrame:")
    print(student)
else:
    print("Column not found; no column deleted.")
