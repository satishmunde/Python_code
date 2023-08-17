str1 = input("Enter a String")

str2=str1[::-1]

if str1 ==  str2:
    print("Palindrome")
else:
    print("Not Palindrome")    
    

# palindrome Number-----------------------------------------

num= int(input("Enter a number1"))
# num2= int(input("Enter a number1"))
temp = num
rev= 0
while num>0:
    r = num%10
    rev = (rev*10)+r
    num = num//10

if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")    
    
