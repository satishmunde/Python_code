num = int(input("Enter a Number"))
rev= 0
while num>0:
    r = num%10
    rev = (rev*10)+r
    num = num//10

print(rev)