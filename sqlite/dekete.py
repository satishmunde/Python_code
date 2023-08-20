import sqlite3

conn = sqlite3.connect('Database.db')

conn.execute(" delete from student where id = 102")
conn.commit()




conn.close()