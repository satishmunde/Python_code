import pymysql

conn =  pymysql.connect(host="localhost", user="root",password="Pass@1234",database="qspider")

cr =  conn.cursor()

cr.execute("create table Student(ID int, Name varchar(20), City varchar(10), Fees int, Marks int)")

cr.close()
  