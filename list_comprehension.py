a = [1,2,3,4,5,6,7,8,9]

#first way-------->
# b = []
# for item in a:
#     if item%2 == 0:
#         b.append(item)
        
# print(b)


#second way -------->
# it will also use for dictonary and set
c = [item for item in a if item%2==0]
print(c)

#list comprehension is nothing but create a list using already created list