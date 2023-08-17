class Employee:
    company = "Google"
    


satish = Employee()
vijay = Employee()
print(satish.company)
print(vijay.company)
Employee.company="YouTube"
print(satish.company)
print(vijay.company)
