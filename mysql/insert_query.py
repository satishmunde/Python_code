import pymysql

try:

    conn =  pymysql.connect(host="localhost",user="root",password="Pass@1234",database="qspider")
    cr = conn.cursor()

    # cr.execute("insert into student values(101,'Satish','Nanded',2000,98)")
    ins = "insert into student values(%s,%s,%s,%s,%s)"
    data=[(102,'Mangesh','Nanded',4000,93),(103,'Kamlesh','Nanded',4400,88)]
    cr.executemany(ins,data) # it execute multiple row operation 
    conn.commit()
    conn.close()
    print("Data inserted successfully")

except Exception as e:
    print(e)
