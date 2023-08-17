class Grand:
    def show1(self):
        print("Inside Grand class")
        
class Parent:
    def show2(self):
        print("Inside Parent class")

class Child(Grand,Parent):   #inside the bracket  which one we mention first, the priority given to them.
    def show3(self):
        print("Inside Child Class")
        
c1 = Child()
c1.show1()
c1.show2()
c1.show3()