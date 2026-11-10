# Q21. Read students.csv containing RollNo, Name, Marks1, Marks2 and Marks3; calculate Total and Percentage; assign grades; display students scoring above 75%; find the student with second-highest percentage; save the result to result.csv.
import pandas as pd

students = pd.read_csv("students.csv")

required_columns = {"RollNo", "Name", "Marks1", "Marks2", "Marks3"}
missing_columns = required_columns - set(students.columns)
if missing_columns:
    raise ValueError(f"students.csv is missing columns: {sorted(missing_columns)}")

students["Total"] = students[["Marks1", "Marks2", "Marks3"]].sum(axis=1)
students["Percentage"] = students["Total"] / 3

# Grade bands are illustrative because the question does not specify a grading scale.
def assign_grade(percentage):
    if percentage >= 90:
        return "A"
    if percentage >= 80:
        return "B"
    if percentage >= 70:
        return "C"
    if percentage >= 60:
        return "D"
    return "F"

students["Grade"] = students["Percentage"].apply(assign_grade)

print("Complete result:")
print(students)
print("\nStudents scoring above 75%:")
print(students[students["Percentage"] > 75])

distinct_percentages = students["Percentage"].drop_duplicates().sort_values(ascending=False)
if len(distinct_percentages) >= 2:
    second_highest = distinct_percentages.iloc[1]
    print("\nStudent(s) with second-highest percentage:")
    print(students[students["Percentage"] == second_highest])
else:
    print("\nSecond-highest percentage is not available.")

students.to_csv("result.csv", index=False)
print("\nResult saved to result.csv")
