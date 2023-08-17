a = 10
def fin1():
    global a
    print(a)
    a=20
    print(a)    

fin1()
print(a)

# it will used to use the global variable  as local variable