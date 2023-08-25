# Write a Python program to find a list of integers containing exactly four distinct values, such that no integer repeats twice consecutively among the first twenty entries.

list =  [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]


for a in range(3,len(list),4):
    print(a)
    l = set()
 
    l = set(list[a-3:a+1])
    print(l)
    if len(l) != 4:
        print(False)
        break
  