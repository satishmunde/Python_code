import pymysql

try:

    conn=pymysql.connect(host="localhost",user="root",password="Pass@1234",database="qspider")

    cr = conn.cursor()

    cr.execute("Update student set name = 'Satish' where id=102")
    conn.commit()

    conn.close()
    print("Data Updated Sucessfully.")

except Exception as e:
    print(e )