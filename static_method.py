class Student:
    college = "MGM's College Nanded"
    def getScode(self):
        print(f"Your College is {self.college} and Your Student Code is {self.code}")
    
    @staticmethod
    def greet():
        print("Good Morning Students")
        
        # in Static  method is use to change the function 
        
        
satish = Student()
satish.code = "1032200159"
satish.getScode()
satish.greet()
