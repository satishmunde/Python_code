import pymysql 


try:
    conn = pymysql.connect(host="localhost",user="root",password="Pass@1234",database="qspider")
    cr = conn.cursor()
    id = int(input("Enter a Student Id"))
    cr.execute(f"select * from student where id = {id}")
    data =  cr.fetchall()
    if len(data) == 0:
        print("Data No Found !")
    else:
        for a in data:
            print(a)
except Exception as e:
    print(e)