# Q17. Create a DataFrame with Roll No, Name, Marks1, Marks2 and Marks3. Calculate total marks and percentage, add Grade based on percentage, display students scoring more than 75%, find the student with second-highest percentage, and sort by percentage.
import pandas as pd

students = pd.DataFrame({
    "Roll No": [101, 102, 103, 104, 105],
    "Name": ["Aarav", "Diya", "Kabir", "Meera", "Rohan"],
    "Marks1": [85, 72, 91, 68, 78],
    "Marks2": [88, 80, 89, 74, 82],
    "Marks3": [90, 76, 95, 70, 85]
})

students["Total Marks"] = students[["Marks1", "Marks2", "Marks3"]].sum(axis=1)
students["Percentage"] = students["Total Marks"] / 3

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

print("Complete student DataFrame:")
print(students)
print("\nStudents scoring more than 75%:")
print(students[students["Percentage"] > 75])

distinct_percentages = students["Percentage"].drop_duplicates().sort_values(ascending=False)
if len(distinct_percentages) >= 2:
    second_highest = distinct_percentages.iloc[1]
    print("\nStudent(s) with second-highest percentage:")
    print(students[students["Percentage"] == second_highest])
else:
    print("\nSecond-highest percentage is not available.")

print("\nDataFrame sorted by percentage (descending):")
print(students.sort_values("Percentage", ascending=False))
