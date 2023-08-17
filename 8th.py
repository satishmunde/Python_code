num = int(input("Enter a Number "))
sum = 0
while num>0:
    re = num%10
    sum =+ (sum*10)+re
    num = num//10
    
print(sum)