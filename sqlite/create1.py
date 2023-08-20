import sqlite3

conn =  sqlite3.connect("Database.db")


# conn.execute('''
#         create table student(
#              Id int primary key,
#              Name varchar(20),
#              Class varchar(15),
#              Email varchar(20)
#         )
# ''')
# conn.execute('''
#         create table studentDetails(
#              Id int primary key,
#              height int,
#              weight int,
#              last_name varchar(20)
#         )
# ''')


conn.close()