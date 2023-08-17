class Number:
    def __init__(self, num):
        self.num = num
        
    def __add__(self, num2):
        return self.num + num2.num

    def __mul__(self, num2):
        return self.num * num2.num
    
    def __sub__(self, num2):
        return self.num - num2.num
    
    def __truediv__(self, num2):
        return self.num / num2.num  
    
    def __floordiv__(self, num2):
        return self.num // num2.num    
num1 = Number(int(input("Enter First Number")))
num2 = Number(int(input("Enter First Number")))
mul = num1 * num2
sum = num1 + num2
sub = num1 - num2
div = num1 / num2
mod = num1 // num2
print(sum)
print(mul)
print(sub)
print(div)
print(mod)