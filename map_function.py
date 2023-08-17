def fun(num):
    return num*num

l=[1,2,3,4,5,6,7,8,9,10]

# method 1 to print all number of square is 

l2 = []
for item in l:
    l2.append(fun(item))
    
print(l2)

# Method 2 to print all number of square is 

print(list(map(fun,l)))