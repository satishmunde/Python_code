for a in range(102):
    # print(a)
    list = []
    while(a>0):
        
        temp= int(a%10)
        
        list.append(temp)
        a=a//10  
    list.reverse()   
    if list.count(0) and list.count(1)== True:
        print(list)
        
        
        