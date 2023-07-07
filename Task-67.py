import sqlite3

authors_data = [('War and Peace', 'Lev Tolstoy', 1865),
                ('And Quiet Flows the Don', 'Mikhail Sholokhov', 1928),
                ('The Brothers Karamazov', 'Fyodor Dostoevsky  ', 1880),
                ('Crime and Punishment', 'Fyodor Dostoevsky', 1866),
                ('KGBT+', 'Viktor Pelevin', 2022)
                ]

conn = sqlite3.connect('authors.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS authors
        (id INTEGER PRIMARY KEY, book_name TEXT, author_name TEXT, year INTEGER)''')
for i in authors_data:

    cursor.execute("INSERT INTO authors (book_name, author_name, year) VALUES (?, ?, ?);",
                   i)
cursor.execute("SELECT * FROM authors WHERE year > 2000")
rows = cursor.fetchall()
for row in rows:
    print(row)