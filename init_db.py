import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, summary) VALUES (?, ?)",
            ('First Post', 'Summary for the first post')
            )

cur.execute("INSERT INTO posts (title, summary) VALUES (?, ?)",
            ('Second Post', 'Summary for the second post')
            )

connection.commit()
connection.close()
