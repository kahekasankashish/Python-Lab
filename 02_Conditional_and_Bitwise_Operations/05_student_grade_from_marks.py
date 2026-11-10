# Q5. Display the grade based on marks: >=90 O, >=80 E, >=70 A, otherwise Fail.
marks = float(input("Enter marks: "))
if marks >= 90:
    grade = "O Grade"
elif marks >= 80:
    grade = "E Grade"
elif marks >= 70:
    grade = "A Grade"
else:
    grade = "Fail"
print("Grade:", grade)
