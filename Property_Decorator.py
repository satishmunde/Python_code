class Employee:
    salary = 5000
    bonous = 800
    
    @property
    def totalSalary(self):
        return self.salary + self.bonous
    # it will run a function like property
    #it is also called @getter
    
    
    
    
e1 = Employee()
print(e1.totalSalary)