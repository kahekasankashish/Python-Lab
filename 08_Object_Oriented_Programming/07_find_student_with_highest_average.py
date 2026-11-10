# Q7. Define a Student class with name, roll, five subject marks, branch and college name. Create 10 Student objects and display the details of the student with the highest average marks.
class Student:
    def __init__(self, studName, studRoll, studMarks, studBranch, studCollegeName):
        if len(studMarks) != 5:
            raise ValueError("Exactly five subject marks are required")
        self.studName = studName
        self.studRoll = studRoll
        self.studMarks = studMarks
        self.studBranch = studBranch
        self.studCollegeName = studCollegeName
        self.average = sum(studMarks) / 5

    def dispStudentDetails(self):
        print(f"Name: {self.studName}")
        print(f"Roll Number: {self.studRoll}")
        print(f"Marks: {self.studMarks}")
        print(f"Average: {self.average:.2f}")
        print(f"Branch: {self.studBranch}")
        print(f"College: {self.studCollegeName}")

students = []
for index in range(10):
    print(f"\nEnter details for student {index + 1}:")
    name = input("Name: ").strip()
    roll = input("Roll number: ").strip()
    marks = list(map(float, input("Enter marks in 5 subjects separated by spaces: ").split()))
    while len(marks) != 5:
        print("Please enter exactly five marks.")
        marks = list(map(float, input("Enter marks in 5 subjects: ").split()))
    branch = input("Branch: ").strip()
    college = input("College name: ").strip()
    students.append(Student(name, roll, marks, branch, college))

top_student = max(students, key=lambda student: student.average)
print("\n*** TOP SCORER ***")
top_student.dispStudentDetails()
