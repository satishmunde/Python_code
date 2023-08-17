class Employee:
    company="Google"
    salary=100
    
    # def changeSal(self,sal):
    #     self.__class__.salary=sal
        
    @classmethod    
    def changeSal(cls,sal):
        cls.salary=sal
        
        #these are two class method to change the value of class variable
        
e1=Employee()
print(e1.salary)
e1.changeSal(4556)
print(e1.salary)
print(Employee.salary)
