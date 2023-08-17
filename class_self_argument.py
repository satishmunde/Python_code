class Employee:
    company = "Google"
    def getSalary(self):
        print("Salary is 10000k")
        
satish=Employee()
# satish.getSalary()

# satish.getSalary()  this code convert in
Employee.getSalary(satish)