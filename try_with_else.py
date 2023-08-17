try:
    a = int(input("Enter a Number"))
    num = 1/a
except Exception as e:
    print("Exception occure")
    print(e)
else:
    print("We are Succesful")
    
    
# If the try block does not throws an exception then else block will execute