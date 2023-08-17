class Calculator:
    def __init__(self,num):
        self.num=num
        print("Object is Created")
        
    def square(self):
        print(f"The Square of {self.num} is {self.num * self.num}")
        
    def squareRoot(self):
        print(f"The Square of {self.num} is {self.num ** 0.5}")
              
    def cube(self):
        print(f"The Square of {self.num} is {self.num * self.num * self.num}")
        
    @staticmethod   
    def greet():
        print("Thanks For Using this Calculator")
        
        
num1 = Calculator(int(input("Enter a Number")))
num1.square()
num1.squareRoot()
num1.cube()
num1.greet()