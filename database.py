import sqlite3

DB_NAME = "students.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            grade TEXT,
            gpa REAL,
            result TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_student(name, grade, gpa, result):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO students
        (name, grade, gpa, result)
        VALUES (?, ?, ?, ?)
    """, (name, grade, gpa, result))

    conn.commit()
    conn.close()