# using with keyword we don't need to close the file 

with open('simple.txt','r') as f:
    a = f.read()
    print(a)

with open('xyz.txt','a') as file:
    a = file.write("Your may go now")