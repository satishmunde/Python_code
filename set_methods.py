#for empty set
b=set()
print(type(b))

#if we declare like that 
a0={}
print(type(a0))
#it will become dictonary
#adding element in set
b.add(1)
b.add(2)
b.add(3)
b.add(4)
b.add(5)
b.add(6)
print(b)

#remove an element
b.remove(6)
print(b)

#pop the element form the set

b.pop()
print(b)

#remove all elements form the elements
b.clear()
print(b)
print(type(b))