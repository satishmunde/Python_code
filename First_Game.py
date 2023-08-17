import random

def game_win(comp,you):
    if comp == you:
        return None
    elif comp =='g':
        if you == 's':
            return False
        elif you == 'w':
            return True
    
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
        
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
        
    else:
        print("Worng choice")



print("Comp Trun : Gun(s), Water(w), Snake(s)")
randomNo=random.randint(1,3)
if randomNo==1:
    comp = 'g'
elif randomNo==2:
    comp = 'w'
elif randomNo==3:
    comp = 's'
    

you=input("Comp Trun : Gun(s), Water(w), Snake(s)")

n=game_win(comp,you)

print(f"Computer Choose : {comp}")
print(f"You Choose : {you}")

if n==None:
    print("It's a Tie") 
elif n:
    print("Your are Win")
else:
    print("Your Loser")