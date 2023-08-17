class Grand:
    def show1(self):
        print("Inside Grand Class")
        
class Parent(Grand):
    def show2(self):
        print("Inside Parent Classes")
        
class Child(Parent):
    def show3(self):
        print("Inside Child Class")
        
c1 = Child()
c1.show1()
c1.show2()
c1.show3()