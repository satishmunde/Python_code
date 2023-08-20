import sqlite3

conn = sqlite3.connect("Database.db")
conn.execute(" update student set name='Satish' where id=101")
conn.commit()
conn.close()