
while(True):
    print("Press q to Quit the Game")
    print("Enter a Number less than 10")
    num = input("Enter a Number ")
    if num == 'q':
        break
    
    try:
        num = int(num)
        if num>10:
            print("You are entered Greater than 10  Number")
            
    except Exception as e:
        print(f"Your Error {e}")
        
print("Thanks for Playing this Cool Game")
        