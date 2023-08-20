from pymysql import*

conn = connect(host="localhost",user="root",password="Pass@1234")
cursor = conn.cursor()

ch = int(input('''
                    Enter Your Choice
                    Press 1 for Create Database
                    Press 2 for Delete Database
               
'''))
if ch == 1:
    try:
        cursor.execute("create database School")
        print("Database Is Created")
    except Exception as e:
        print(e)
elif ch == 2:
        
    try:
        cursor.execute("drop database School")
        print("Database Dropped")

    except Exception as e:
        print(e)