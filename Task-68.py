import sqlite3

movies_data = [('Зеленая миля', 'драма', 9.2),
                ('Побег из Шоушенка', 'драма', 9.0),
                ('Тайна Коко', 'мультфильм', 8.9),
                ('Бойцовский клуб', 'триллер', 8.8),
                ('Иван Васильевич меняет профессию', 'комедия', 8.8)
                ]

conn = sqlite3.connect('movies.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS movies
        (id INTEGER PRIMARY KEY, name TEXT, genre TEXT, rating FLOAT)''')
for i in movies_data:

    cursor.execute("INSERT INTO movies (name, genre, rating) VALUES (?, ?, ?);",
                   i)
cursor.execute("SELECT * FROM movies WHERE genre = 'драма'")
rows = cursor.fetchall()
for row in rows:
    print(row)