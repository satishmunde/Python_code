class Parent:
    num=10
    
    def parentClass(self):
        print("Inside Parent class")
        
class Child(Parent):
    num1=20
    
    def addition(self):
        return self.num + self.num1

c1 = Child()
c1.parentClass()
sum = c1.addition()

print(sum)