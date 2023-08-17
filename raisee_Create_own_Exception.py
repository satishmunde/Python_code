#using this raise keyword we can create our own exception 

def increment(num):
    try:
        return int(num) + 1
    
    except:
        raise ValueError("You have entered String value")
    

a = increment(input("Enter a number"))
print(a)