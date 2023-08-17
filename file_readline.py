# it will read single line at once
f = open('xyz.txt')
data=f.readline()
print(data)
data=f.readline()
print(data)
data=f.readline()
print(data)

f.close()