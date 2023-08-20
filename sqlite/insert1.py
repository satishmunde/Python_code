import sqlite3

conn =  sqlite3.connect("Database.db")


conn.execute('''
        insert into student values(102,'Mangsh','BSC','Mangesh@gmail.com')
''')


conn.execute('''
        insert into studentDetails values(101,167,74,'Munde'),(102,54,167,'Tambde')
''')


conn.commit()
conn.close()