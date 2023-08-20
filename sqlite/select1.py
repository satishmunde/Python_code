import sqlite3

conn =  sqlite3.connect("Database.db")
data= conn.execute("Select * from studentDetails ")  #limit 1,1

for a in data:
    print(a[0]," ", a[1]," ",a[2]," ",a[3]," ")

conn.close()