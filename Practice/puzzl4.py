# Write a Python program to check a given list of integers where the sum of the first i integers is i.
# Input:
# [0, 1, 2, 3, 4, 5]
# Output:
# False
# Input:
# [1, 1, 1, 1, 1, 1]
# Output:
# True
# Input:
# [2, 2, 2, 2, 2]
# Output:
# False

list = [0,2,3,4,5]


i = list[0]
if sum(list[:i] )== list[0]:
    print(True)
else:
    print(False)