#  Write a Python program to split a string of words separated by commas and spaces into two lists, words and separators.
# Input: W3resource Python, Exercises.
# Output:
# [['W3resource', 'Python', 'Exercises.'], [' ', ', ']]
# Input: The dance, held in the school gym, ended at midnight.
# Output:
# [['The', 'dance', 'held', 'in', 'the', 'school', 'gym', 'ended', 'at', 'midnight.'], [' ', ', ', ' ', ' ', ' ', ' ', ', ', ' ', ' ']]
i ='The colors in my studyroom are blue green and yellow.'
# Output:
# [['The', 'colors', 'in', 'my', 'studyroom', 'are', 'blue', 'green', 'and', 'yellow.'], [' ', ' ', ' ', ' ', ' ', ' ', ', ', ', ', ' ']]

list = i.split(" ")
print(list)
list1 = []
for a in range(len(list)-1):
    list1.append(" ")

list.append(list1)
print(list)



