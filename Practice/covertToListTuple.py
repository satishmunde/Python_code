# Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
values = '1,2,3,4,5,6,7,8'


list = values.split(",")
print( list)
tuple = tuple(list)
print(tuple)