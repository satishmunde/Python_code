import pymysql 


try:
    conn = pymysql.connect(host="localhost",user="root",password="Pass@1234",database="qspider")
    cr = conn.cursor()

    cr.execute("Select * from student order by id asc limit 1,1")
    # order by  desc or asc
    # limit : -  we have pass the limit after the order by clause 
    # syn : - limit 1,2
    # first argument represents the postion of data 
    # second argumrnt represents the size of data 



    data = cr.fetchall()
    for a in data:
        print(a)

except Exception as e:
    print(e)