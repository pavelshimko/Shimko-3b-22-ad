import sqlite3

students_data = [('Andrew', 21, 4.3),
                ('Max', 20, 4.2),
                ('Andrew', 22, 3.1),
                ('Andrew', 22, 3.9)]
conn = sqlite3.connect('students.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS students
        (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, grade FLOAT)''')
for i in students_data:

    cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?);",
                   i)
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
for row in rows:
    print(row)