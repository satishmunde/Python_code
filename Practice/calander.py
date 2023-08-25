import calendar
y = int(input("Input the year : "))
m = int(input("Input the month : "))
print(calendar.month(y, m))

for m in range(1,13):
    
    print(calendar.month(y,m))