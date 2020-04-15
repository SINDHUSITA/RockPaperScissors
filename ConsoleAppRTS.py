def limitedMode():
    print("Best of 7 or 5 or 3?")
    global numberOfGames
    numberOfGames=int(input())
    while(numberOfGames!=7 and numberOfGames!=5 and numberOfGames!=3):
        print("PLease enter 7 or 5 or 3")
        numberOfGames=int(input())

def unlimitedMode():
    global numberOfGames
    numberOfGames=sys.maxsize 

options=['none','Rock','Paper','Scissors']
computerScore=0
myScore=0
import random
import sys

#Choosing Mode
print("Select Mode of Play: \n1. Limited 2. Unlimited")
mode=int(input())
while(mode!=1 and mode!=2):
    print("PLease Enter Mode as 1 or 2 only")
    mode=int(input())

#functions based on mode    
if(mode==1):
    limitedMode()    
else:
    unlimitedMode()    

#Iterating for rounds
while((computerScore<(int(numberOfGames/2)+1)) and (myScore<(int(numberOfGames/2)+1))):
    #Player Choice Generation
    print('Select your choice:\n1. Rock 2. Paper 3. Scissors',end=" ")
    if(mode==2):
        print("0. To exit")
    myChoice=int(input())
    if(myChoice not in range(0,4)):
        print("Please enter right choice")
    elif(myChoice==0):
        break
    else:        
        #Computer Choice Generation
        computerChoice=random.randint(1,3)        
        print("\nYour Choice: ",options[myChoice])
        print("Computer Choice: ",options[computerChoice],'\n')
        
        #Check choice and inc score
        if(myChoice==1 and computerChoice==2):
            computerScore=computerScore+1
            print("Point to Computer\nComputer Score: ",computerScore,"\nYour Score: ",myScore)
        elif(myChoice==2 and computerChoice==3):
            computerScore=computerScore+1
            print("Point to Computer\nComputer Score: ",computerScore,"\nYour Score: ",myScore)
        elif(myChoice==3 and computerChoice==1):
            computerScore=computerScore+1
            print("Point to Computer\nComputer Score: ",computerScore,"\nYour Score: ",myScore)
        elif(myChoice==3 and computerChoice==2):
            myScore=myScore+1
        elif(myChoice==computerChoice):
            print("No one scores\nComputer Score: ",computerScore,"\nYour Score: ",myScore)   
        else:
            myScore=myScore+1
            print("Point to You\n\nComputer Score: ",computerScore,"\nYour Score: ",myScore)
if(computerScore>myScore):
    print("Computer Wins!!!")
else:
    print("You Win!!!")