import sqlite3
from flask import g

admins = [
    "Karim",
    "Mehdi",
]

admins = sorted(admins)

connection = sqlite3.connect("data/admin_data_handler.sqlite")
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS admins (name TEXT)")
cursor.executemany("INSERT INTO admins VALUES (?)", [(admin,) for admin in admins])

commit = connection.commit()

for row in cursor.execute("SELECT * FROM admins"):
    print(row)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect("data/admin_data_handler.sqlite")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM admins")
    return cursor.fetchall()

connection.close()