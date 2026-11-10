# Question 13: Input marks in five subjects and print the average mark.
marks = []
for i in range(1, 6):
    marks.append(float(input(f"Enter marks in subject {i}: ")))

average = sum(marks) / len(marks)
print("Average marks:", average)
