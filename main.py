'''
water = -1
snake =1
gun=0
'''
import random
computer=random.choice([-1,1,0])
you=input("Enter your choose = ")
youdict={"w":-1,"s":1,"g":0}
reversedict={-1:"Water", 1:"Snake",0:"Gun"}
n=youdict[you]
print(f"Your Choose {reversedict[n]}\n Computer Choose {reversedict[computer]}")
if(computer==n):
    print("Match is draw!")
else:
    if(computer==1 and n==-1):
        print("You win!")
    elif(computer==1 and n==0):
        print("You win!")
    elif(computer==-1 and n==1):
        print("You lose!")  
    elif(computer==-1 and n==0):
        print("You lose!")
    elif(computer==0 and n==1):
        print("You lose!")
    elif(computer==0 and n==-1):
        print("You win!")    
    else:
        print("Some thing wrong!")    
                