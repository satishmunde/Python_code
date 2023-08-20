import sqlite3
conn = sqlite3.connect("Database.db")
ch = int(input(''' Enter your choice of serch
          By ID Press 1
          By Name Press 2'''))

if ch == 1:
    id = input("Please the the id that Data You Want to See  -- >  ")
    data= conn.execute("select * from student where id="+id)
    data1 = data.fetchone()

    if not data1:
        print("Data Not Found ! ")

    else:
        print("Your Data Is Found -- > ")
        print("Id -- Name -- Class -- Email--")
        for a in data1:

            print(a ,end='--')

elif ch == 2:
    name = input("Please Enter Student Name")
    data =  conn.execute(f'''select * from student where name like '%{name}%' ''')
    data = data.fetchall()
    if not data:
        print("Data Not Found ! ")
    else:

        for a in data:
            print(a," ")
conn.close()