try:
    a = int(input("Enter a number"))
    num = 1/a
    
except Exception as e:
    print(e)
    exit()
    
finally:
    print("Finally clause is Execute...")
    
#the finally clause always execute if the exception is occure or programs get exits