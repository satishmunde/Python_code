# 1. Write a Python program to find a list of integers with exactly two occurrences of nineteen and at least three occurrences of five. Return True otherwise False.
# Input:
# [19, 19, 15, 5, 3, 5, 5, 2]
# Output:
# True
# Input:
# [19, 15, 15, 5, 3, 3, 5, 2]
# Output:
# False
# Input:
# [19, 19, 5, 5, 5, 5, 5]
# Output:
# True

list = [19, 19, 15, 5, 3, 5, 1, 2]
print(list)
if list.count(19) >= 2 and list.count(5) >= 3:
    print("True")
else:
    print(False)


#  Write a Python program that accepts a list of integers and calculates the length and the fifth element. Return true if the length of the list is 8 and the fifth element occurs thrice in the said list.
# Input:
# [19, 19, 15, 5, 5, 5, 1, 2]
# Output:
# True
# Input:
# [19, 15, 5, 7, 5, 5, 2]
# Output:
# False
# Input:
# [11, 12, 14, 13, 14, 13, 15, 14]
# Output:
# True
# Input:
# [19, 15, 11, 7, 5, 6, 2]
# Output:
# False


list = [19, 19, 15, 5, 5, 5, 1, 2]
print(list)
if(len(list) is 8 and list.count(list[5]) is 3):
    print(True)
else:
    print(False)