
# Write a Python program that accepts an integer and determines whether it is greater than 4^4 and which is 4 mod 34.
# Input:
# 922
# Output:
# True
# Input:
# 914
# Output:
# False
# Input:
# 854
# Output:
# True
# Input:
# 854
# Output:
# True

num =  int(input("Enter a Number "))
if num>4**4 and num%34 ==4:
    print ("True")
else:
    print(False)