import sqlite3

movies_data = [('Колосов Глеб Платонович', 'генеральный директор', 200000),
                ('Алексеев Георгий Ильич', 'заместитель директора', 120000),
                ('Леонтьева Анна Львовна', 'менеджер по продажам', 98000),
                ('Ермолаев Михаил Артурович', 'менеджер по продажам', 90000),
                ('Панов Никита Дмитриевич', 'менеджер по продажам', 90000)
                ]

conn = sqlite3.connect('employees.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS employees
        (id INTEGER PRIMARY KEY, name TEXT, position TEXT, salary FLOAT)''')
for i in movies_data:

    cursor.execute("INSERT INTO employees (name, position, salary) VALUES (?, ?, ?);",
                   i)
cursor.execute("SELECT * FROM employees WHERE position = 'менеджер по продажам'")
rows = cursor.fetchall()
for row in rows:
    print(row)