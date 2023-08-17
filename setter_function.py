class Employee:
    salary = 5000
    bonous = 800
    totalSalary=0
     
    
    @totalSalary.setter
    def totalSalary(self, val):
        self.bonous = val - self.salary
  
e1 = Employee()
e1.totalSalary = 6800
print(e1.salary)
print(e1.bonous)