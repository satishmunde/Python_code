# def fab(n):
#   a=0
#   b=1
#   print(a)
#   while(b<n):
#     print(b)
#     # c=a+b
#     # a=b
#     # b=c
    
#     a,b= b,a+b
    
# fab(10)

# using Recursion-----------------------------------------------> 

def fab(n):
  if n<=1:
    return n
  else:
    return (fab(n-1)+fab(n-2))
  
  
n=10

if n<=0:
  print("Invalid")
else:
  for i in range(n):
    print(fab(i))