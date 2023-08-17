num= int(input("Enter a Number"))
prime = True
for a in range(2,num):
    
    if(num%a == 0):
        prime = False
        break


    if  prime:
     print(" It is Prime Number")
    
    else:
        print("It is not Prime Number")
        
   
        
     