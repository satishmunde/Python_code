content=True
i=0
with open("simple.txt",'r') as f:
    while content:
       content = f.readline()
       i+=1
       if "Sattu's" in content:
           print(content)
           print(f"{content} is present in {i}")
        

    