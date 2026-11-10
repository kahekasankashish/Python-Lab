# Q18. Using NumPy: (1) create a 2D array for marks of 6 students in 4 subjects (user input); (2) compute total and average marks for each student; (3) display students scoring above 70%; (4) find the student with the second highest total marks; (5) display subject-wise highest marks.
import numpy as np

marks = []
for student in range(6):
    row = list(map(float, input(f"Enter marks for student {student + 1} in 4 subjects: ").split()))
    if len(row) != 4:
        raise ValueError("Enter exactly four marks for each student.")
    if any(mark < 0 or mark > 100 for mark in row):
        raise ValueError("Marks must be between 0 and 100.")
    marks.append(row)

marks_array = np.array(marks)
totals = marks_array.sum(axis=1)
averages = marks_array.mean(axis=1)
print("Marks:\n", marks_array)
for index, (total, average) in enumerate(zip(totals, averages), start=1):
    print(f"Student {index}: total={total:.2f}, average={average:.2f}")

print("Students scoring above 70% (average > 70):", (np.where(averages > 70)[0] + 1).tolist())
distinct_totals = np.unique(totals)
if len(distinct_totals) < 2:
    print("Second-highest total: Not available (fewer than two distinct totals).")
else:
    second_highest = distinct_totals[-2]
    print("Student(s) with second-highest total:", (np.where(totals == second_highest)[0] + 1).tolist())
    print("Second-highest total marks:", second_highest)
print("Subject-wise highest marks:", marks_array.max(axis=0))
