from ast import main
from threading import main_thread


def max(num1,num2,num3):
    if num1>num2 and num1>num3 :
        print(f"Greatest number is {num1}")
    elif num2>num1 and num2>num3:
        print(f"Greatest number is {num2}")
    else:
        print(f"Greatest Number is {num3}")
        
if __name__=="__main__":
    num1=int(input("Enter First Number"))
    num2=int(input("Enter Second Number"))
    num3=int(input("Enter Third Number"))
    max(num1,num2,num3)
