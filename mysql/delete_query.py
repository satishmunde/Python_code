import pymysql 


try:
    conn = pymysql.connect(host="localhost",user="root",password="Pass@1234",database="qspider")
    cr = conn.cursor()
    
    cr.execute("Delete from student where id = 101")
    conn.commit()
    cr.close()
    print("Data Deleted ")

except Exception as e:
    print(e)
