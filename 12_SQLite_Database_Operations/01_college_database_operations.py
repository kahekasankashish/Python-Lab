# Assignment 12
# Write a Python program to perform the following database operations:
# 1. Create college.db with student and result tables.
# 2. Insert five user-provided records into each table using parameterized queries and commit.
# 3. Retrieve and display all records from both tables.
# 4. Display students whose fees are greater than 50000.
# 5. Display students whose marks are greater than 75 in all subjects.
# 6. Display the result of a given subject.
# 7. Add grade TEXT to result and assign grades based on marks.
# 8. Update marks of a student in a specified subject.
# 9. Delete records from result based on subject.
# 10. Display the final tables.

import sqlite3

DATABASE_NAME = "college.db"


def display_rows(title, rows):
    print(f"\n{title}")
    if not rows:
        print("No records found.")
        return
    for row in rows:
        print(row)


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS student (
            rollno INTEGER PRIMARY KEY,
            name TEXT,
            dob TEXT,
            fee REAL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS result (
            rollno INTEGER,
            subject TEXT,
            marks REAL,
            FOREIGN KEY (rollno) REFERENCES student(rollno)
        )
    """)

    connection.commit()


def insert_students(connection):
    print("\nEnter details of 5 students.")
    records = []
    for index in range(5):
        print(f"\nStudent {index + 1}")
        rollno = int(input("Roll number: "))
        name = input("Name: ").strip()
        dob = input("Date of birth (YYYY-MM-DD): ").strip()
        fee = float(input("Fee paid: "))
        records.append((rollno, name, dob, fee))

    connection.executemany(
        "INSERT INTO student (rollno, name, dob, fee) VALUES (?, ?, ?, ?)",
        records
    )
    connection.commit()
    print("Student records inserted successfully.")


def insert_results(connection):
    print("\nEnter 5 result records.")
    records = []
    for index in range(5):
        print(f"\nResult record {index + 1}")
        rollno = int(input("Student roll number: "))
        subject = input("Subject name: ").strip()
        marks = float(input("Marks obtained: "))
        records.append((rollno, subject, marks))

    connection.executemany(
        "INSERT INTO result (rollno, subject, marks) VALUES (?, ?, ?)",
        records
    )
    connection.commit()
    print("Result records inserted successfully.")


def display_all_records(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM student")
    display_rows("STUDENT TABLE", cursor.fetchall())

    cursor.execute("SELECT * FROM result")
    display_rows("RESULT TABLE", cursor.fetchall())


def display_students_fee_above_50000(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM student WHERE fee > ?", (50000,))
    display_rows("STUDENTS WHOSE FEES ARE GREATER THAN 50000", cursor.fetchall())


def display_students_above_75_in_all_subjects(connection):
    cursor = connection.cursor()
    cursor.execute("""
        SELECT s.rollno, s.name, s.dob, s.fee
        FROM student AS s
        JOIN result AS r ON s.rollno = r.rollno
        GROUP BY s.rollno, s.name, s.dob, s.fee
        HAVING MIN(r.marks) > 75
    """)
    display_rows(
        "STUDENTS SCORING MORE THAN 75 IN ALL RECORDED SUBJECTS",
        cursor.fetchall()
    )


def display_result_for_subject(connection):
    subject = input("\nEnter subject name to view its result: ").strip()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT s.rollno, s.name, r.subject, r.marks
        FROM student AS s
        JOIN result AS r ON s.rollno = r.rollno
        WHERE r.subject = ?
    """, (subject,))
    display_rows(f"RESULT FOR SUBJECT: {subject}", cursor.fetchall())


def add_grade_column_and_assign_grades(connection):
    cursor = connection.cursor()
    columns = [row[1] for row in cursor.execute("PRAGMA table_info(result)").fetchall()]

    if "grade" not in columns:
        cursor.execute("ALTER TABLE result ADD COLUMN grade TEXT")

    cursor.execute("""
        UPDATE result
        SET grade = CASE
            WHEN marks >= 90 THEN 'A'
            WHEN marks >= 75 THEN 'B'
            WHEN marks >= 50 THEN 'C'
            ELSE 'F'
        END
    """)
    connection.commit()
    print("\nGrade column added (if needed) and grades assigned.")


def update_student_marks(connection):
    rollno = int(input("\nEnter student roll number: "))
    subject = input("Enter subject name: ").strip()
    marks = float(input("Enter updated marks: "))

    cursor = connection.cursor()
    cursor.execute("""
        UPDATE result
        SET marks = ?
        WHERE rollno = ? AND subject = ?
    """, (marks, rollno, subject))

    if cursor.rowcount == 0:
        print("No matching result record found.")
    else:
        # Keep the grade consistent with the updated marks.
        cursor.execute("""
            UPDATE result
            SET grade = CASE
                WHEN marks >= 90 THEN 'A'
                WHEN marks >= 75 THEN 'B'
                WHEN marks >= 50 THEN 'C'
                ELSE 'F'
            END
            WHERE rollno = ? AND subject = ?
        """, (rollno, subject))
        print("Marks updated successfully.")

    connection.commit()


def delete_results_by_subject(connection):
    subject = input("\nEnter subject name whose result records should be deleted: ").strip()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM result WHERE subject = ?", (subject,))
    deleted_count = cursor.rowcount
    connection.commit()
    print(f"{deleted_count} result record(s) deleted.")


def main():
    connection = sqlite3.connect(DATABASE_NAME)
    try:
        # Enforce the declared foreign-key relationship in SQLite.
        connection.execute("PRAGMA foreign_keys = ON")

        create_tables(connection)
        print(f'Database "{DATABASE_NAME}" and required tables are ready.')

        insert_students(connection)
        insert_results(connection)

        display_all_records(connection)
        display_students_fee_above_50000(connection)
        display_students_above_75_in_all_subjects(connection)
        display_result_for_subject(connection)

        add_grade_column_and_assign_grades(connection)
        update_student_marks(connection)
        delete_results_by_subject(connection)

        display_all_records(connection)
        print("\nAll database operations completed.")
    except sqlite3.IntegrityError as error:
        connection.rollback()
        print("Database integrity error:", error)
        print("Check that each result roll number exists in the student table and that roll numbers are not duplicated.")
    except (ValueError, sqlite3.Error) as error:
        connection.rollback()
        print("An error occurred:", error)
    finally:
        connection.close()


if __name__ == "__main__":
    main()
