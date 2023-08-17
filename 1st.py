
def sum_first(n):
    if n > 0:
        sum = n + sum_first(n-1)
        return sum
    else:
        return 0


num= int(input("Enter The renge of Natural number"))
sum =sum_first(num)
print(sum)