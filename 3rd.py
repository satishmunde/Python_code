
n = int(input("enter a Number"))

sum=0
temp=n

while(n>0):
    r = n%10
    sum+=r**3
    n= n//10
if temp==sum:
    print(f"{temp} is Armstrong Number")
else:
    print(f"{temp} is not Armstorng Number")
