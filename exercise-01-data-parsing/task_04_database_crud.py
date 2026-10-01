import sqlite3
import os

# -------------------------------------------------------------
# Exercise 4: Relational Database Design and CRUD Operations
# -------------------------------------------------------------

DB_FILE = "student_portal.db"

def init_database(db_path=DB_FILE):
    """Creates normalized relational schema with Foreign Key constraints."""
    if os.path.exists(db_path):
        os.remove(db_path)

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")

    # 1. Departments Table
    cursor.execute("""
        CREATE TABLE departments (
            department_id INTEGER PRIMARY KEY AUTOINCREMENT,
            department_name TEXT NOT NULL UNIQUE,
            building TEXT
        );
    """)

    # 2. Students Table
    cursor.execute("""
        CREATE TABLE students (
            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            department_id INTEGER,
            gpa REAL CHECK (gpa >= 0.0 AND gpa <= 4.0),
            enrollment_date TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (department_id) REFERENCES departments(department_id) ON DELETE SET NULL
        );
    """)

    # 3. Courses Table
    cursor.execute("""
        CREATE TABLE courses (
            course_id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_code TEXT UNIQUE NOT NULL,
            title TEXT NOT NULL,
            credits INTEGER CHECK (credits > 0),
            department_id INTEGER,
            FOREIGN KEY (department_id) REFERENCES departments(department_id) ON DELETE CASCADE
        );
    """)

    # 4. Enrollments (Junction Table for M:N Relationship)
    cursor.execute("""
        CREATE TABLE enrollments (
            enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            course_id INTEGER NOT NULL,
            semester TEXT NOT NULL,
            grade TEXT,
            FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
            FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE,
            UNIQUE(student_id, course_id, semester)
        );
    """)

    conn.commit()
    conn.close()
    print("Database schema created with relational integrity & foreign keys.")


# -------------------------------------------------------------
# CRUD Operations
# -------------------------------------------------------------

# C - CREATE
def create_records(db_path=DB_FILE):
    print("\n" + "=" * 60)
    print("1. CREATE (Insert Initial Records)")
    print("=" * 60)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")

    # Insert Departments
    dept_data = [
        ("Computer Science", "Turing Hall"),
        ("Electrical Engineering", "Tesla Building"),
        ("Mathematics", "Euler Center")
    ]
    cursor.executemany("INSERT INTO departments (department_name, building) VALUES (?, ?)", dept_data)

    # Insert Students
    student_data = [
        ("Alice Smith", "alice.smith@university.edu", 1, 3.85),
        ("Bob Jones", "bob.jones@university.edu", 1, 3.20),
        ("Charlie Brown", "charlie.b@university.edu", 2, 3.50),
        ("Diana Prince", "diana.p@university.edu", 3, 3.95)
    ]
    cursor.executemany("INSERT INTO students (name, email, department_id, gpa) VALUES (?, ?, ?, ?)", student_data)

    # Insert Courses
    course_data = [
        ("CS101", "Intro to Programming", 4, 1),
        ("CS201", "Data Structures", 4, 1),
        ("EE101", "Circuit Analysis", 3, 2),
        ("MATH201", "Linear Algebra", 3, 3)
    ]
    cursor.executemany("INSERT INTO courses (course_code, title, credits, department_id) VALUES (?, ?, ?, ?)", course_data)

    # Enroll Students
    enroll_data = [
        (1, 1, "Fall 2026", "A"),
        (1, 2, "Fall 2026", "A-"),
        (2, 1, "Fall 2026", "B+"),
        (3, 3, "Fall 2026", "A"),
        (4, 4, "Fall 2026", "A")
    ]
    cursor.executemany("INSERT INTO enrollments (student_id, course_id, semester, grade) VALUES (?, ?, ?, ?)", enroll_data)

    conn.commit()
    conn.close()
    print("Populated departments, students, courses, and enrollments.")


# R - READ
def read_records(db_path=DB_FILE):
    print("\n" + "=" * 60)
    print("2. READ (Querying with Relational JOINs)")
    print("=" * 60)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    query = """
        SELECT
            s.student_id,
            s.name AS student_name,
            d.department_name,
            s.gpa,
            c.course_code,
            c.title AS course_title,
            e.grade
        FROM students s
        LEFT JOIN departments d ON s.department_id = d.department_id
        LEFT JOIN enrollments e ON s.student_id = e.student_id
        LEFT JOIN courses c ON e.course_id = c.course_id
        ORDER BY s.student_id, c.course_code;
    """
    cursor.execute(query)
    rows = cursor.fetchall()

    print(f"{'ID':<4} | {'Student Name':<15} | {'Department':<20} | {'GPA':<4} | {'Course':<8} | {'Title':<22} | {'Grade':<5}")
    print("-" * 90)
    for r in rows:
        c_code = r[4] if r[4] else "N/A"
        c_title = r[5] if r[5] else "Not Enrolled"
        grade = r[6] if r[6] else "-"
        print(f"{r[0]:<4} | {r[1]:<15} | {r[2]:<20} | {r[3]:<4.2f} | {c_code:<8} | {c_title:<22} | {grade:<5}")

    conn.close()


# U - UPDATE
def update_records(db_path=DB_FILE):
    print("\n" + "=" * 60)
    print("3. UPDATE (Modify Existing Records)")
    print("=" * 60)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")

    # 1. Update Bob's GPA
    cursor.execute("UPDATE students SET gpa = ? WHERE email = ?", (3.45, "bob.jones@university.edu"))
    print(f"Updated Bob Jones GPA -> Rows affected: {cursor.rowcount}")

    # 2. Update Enrollment Grade for Alice in CS201
    cursor.execute("""
        UPDATE enrollments
        SET grade = 'A+'
        WHERE student_id = (SELECT student_id FROM students WHERE email = 'alice.smith@university.edu')
          AND course_id = (SELECT course_id FROM courses WHERE course_code = 'CS201')
    """)
    print(f"Updated Alice Smith grade for CS201 to 'A+' -> Rows affected: {cursor.rowcount}")

    conn.commit()
    conn.close()


# D - DELETE
def delete_records(db_path=DB_FILE):
    print("\n" + "=" * 60)
    print("4. DELETE (Removing Records with Referential Cascade)")
    print("=" * 60)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")

    # Remove student Charlie Brown
    cursor.execute("DELETE FROM students WHERE email = ?", ("charlie.b@university.edu",))
    print(f"Deleted student Charlie Brown -> Rows affected: {cursor.rowcount}")

    # Verify cascade deletion in enrollments
    cursor.execute("SELECT COUNT(*) FROM enrollments WHERE student_id = 3")
    cascade_count = cursor.fetchone()[0]
    print(f"Enrollments remaining for student_id 3 (Cascade Verified): {cascade_count}")

    conn.commit()
    conn.close()


def main():
    init_database()
    create_records()
    read_records()
    update_records()
    delete_records()
    print("\n" + "=" * 60)
    print("Final State after CRUD operations:")
    print("=" * 60)
    read_records()
    print("\nExercise 4 Complete: Database design and CRUD operations verified.")


if __name__ == "__main__":
    main()
