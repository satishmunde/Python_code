def remove_(string,word):
    new_str=string.replace(word,"")
    return new_str.strip()

name= "Hii this is Satish Munde"
n=remove_(name,"Satish")
print(n)