import os
class bike:


    def __init__(self,stock):
        self.stock = stock
    
    def showBike(self):
        print("Available Bikes are ",self.stock)

    def rentBike(self,q):
        if self.stock == 0:
            print("Bikes Are Not Available")
        elif q<=0:
            print("Please enter the Quantity in positive value")
        elif q>self.stock:
            print("Please enter the Quantity below the stock")
            print("Available Bikes are ",self.stock)

        else:
            self.stock=self.stock-q
            print("Total Price is",q*100)
            print("Available Quantity is ",self.stock)
        
obj=bike(int(input("Enter The Quentity of your Bike")))
while True:
    
    ch=int(input(''' 
        Press 1  to see the Quantity
        Press 2 Take bike on Rent
        Press 3 to Exit'''))
    
    if ch==1:
        os.system('cls')
        obj.showBike()
    elif ch==2:
        os.system('cls')
        obj.rentBike(int(input("Enter a Quantity of Bike")))
    elif ch==3:
        break
    


