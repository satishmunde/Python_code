num = int(input("Enter a Number"))
temp = num
rev= 0
while num>0:
    r = num%10
    rev = (rev+(r*r*r))
    num = num//10

if temp == rev:
    print("ArmStrong")
else:
    print("Not ArmStrong")    
    
