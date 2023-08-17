class Grand:
    def show1(self):
        print("Inside Grand Show 1 Class")
        
class Parent(Grand):
    def show2(self):
        super().show1()
        print("Inside Parent Show 2 Classes")
        
class Child(Parent):
    def show3(self):
        super().show2()
        print("Inside Child  Show 3 Class")
        
c1 = Child()
c1.show1()
c1.show2()
c1.show3()