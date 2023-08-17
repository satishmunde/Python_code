#if we need to get  items with it index  the we can use enumerate function

list1= [11,False,True,44.3,"Satish"]

for i,item in enumerate(list1):
    print(f"{i}-----------{item}")
    
# for i,item in list1:
#     print(f"{i}-----------{item}")
# #this will generate the error below 


#    for i,item in list1:
# TypeError: cannot unpack non-iterable int object