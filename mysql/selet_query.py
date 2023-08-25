import pymysql


try:
    conn = pymysql.connect(host="localhost",user="root",password="Pass@1234",database="qspider")
    cr = conn.cursor()
    cr.execute("select * from student")

    print("{:<20} {:<20}{:<20}{:<20}{:<20}".format("Student ID","Student Name","Student Class","Student Fees","Student Marks"))

    data = cr.fetchall()

    for a in data:
        print("{:^20}{:^20}{:^20}{:^20}{:^20}".format(a[0],a[1],a[2],a[3],a[4]))

except Exception as e:
    print(e)

