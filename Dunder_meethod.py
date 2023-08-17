class Number:
    # to perform operator overloading there are special function
    
    def __init__(self, num):
        self.num = num
        
        #it is dunder method that will call when direct object is print.
    def __str__(self):
        return f"The Number is {self.num}"
            
  
    
num1 = Number(5)
print(num1)