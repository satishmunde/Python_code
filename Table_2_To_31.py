for i in range(2,31):
    with open(f"Table_of_{i}.txt",'w') as f:
        for j in range(1,11):
            f.write(f"{i} X {j} = {i*j}\n")
            
                


    