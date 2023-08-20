import sqlite3

conn =  sqlite3.connect("Database.db")

# data = conn.execute(''' 
#                 select * from student left join StudentDetails on  Student.id = StudentDetails.id
# ''')

# for Specic data

data = conn.execute(''' 
                select s1.name,d1.last_name,s1.class from student s1 , StudentDetails d1 on  s1.id = d1.id
''')


for a in data:
    print(a[0],"  ", a[1],"  ",a[2])