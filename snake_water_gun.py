# Making snake water gun
import random
def Gamewin(a,b):
    # if two values are equal declare tie
    if a == b:
        return None

            # check all posibility when computer chose s
    elif a == 's':
        if b == 'w':
            return False
        elif b == 'g':
            return True

            # check all posibility when computer chose w
        elif a == 'w':
         if b == 'g':
            return False
        elif b == 's':
            return True
            
            # check all possibility when computer chose g
            
        elif a == 'g':
         if b == 's':
            return False
        elif b== 'w':
            return True

print("Comp Turn: Snake(s) Water(w) or Gun(g)")    
randomNo = random.randint(1,3)    
if randomNo == 1:
    a = 's'
elif randomNo == 2:
    a = 'w'
elif randomNo == 3:
    a = 'g'

b=input("Your Turn: Snake(s) Water(w) or Gun(g)")
c = Gamewin(a,b)
print(f"Comp Chose {a}")
print(f"You Chose {b}")
if c == None:
    print("The game is a tie")
elif c:
    print("You Win!")
else:
    print("You loose!")


    
    




    






