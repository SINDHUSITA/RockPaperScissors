numberOfGames=0
mode=2
myChoice=0
computerScore=0
myScore=0
computerChoice=0
options=['none','Rock','Paper','Scissors']

def setMyChoice(val):
    global myChoice
    global myScore
    global computerScore
    myChoice=val
    s="Your choice is: "+options[val]
    tkMyChoice.set(s)
    incScore()
    if((computerScore<(int(numberOfGames/2)+1)) and (myScore<(int(numberOfGames/2)+1))):
        showRPS()
    else:
        displaywinner()
        
def setNumberOfGames(val):
    tkWinner.set("")
    tkComputerScore.set("Computer's Score: 0")
    tkMyScore.set("Your Score: 0")
    tkComputerChoice.set("")
    tkMyChoice.set("")    

    global numberOfGames
    numberOfGames=val
    count.set(numberOfGames)
    if(numberOfGames<10):
        EndButton.grid_forget()
    else:
        EndButton.grid(row=7,column=2)
    showRPS()
    
def displaywinner():
    global computerScore
    global myScore
    if(computerScore>myScore):
        s="Computer Wins!!!"
        tkWinner.set(s)
    elif(computerScore==myScore):
        s="Draw Match! Play Again!!"
        tkWinner.set(s)
    else:
        s="You Win!!!"
        tkWinner.set(s)
    myScore=0
    computerScore=0
    RockButton.grid_forget()
    PaperButton.grid_forget()
    ScissorsButton.grid_forget()
    EndButton.grid_forget()

def showRPS():
    global computerScore
    global myScore
    
    ChoiceLabel.grid(row=5,columnspan=2,rowspan=1,column=0)
    RockButton.grid(row=6,column=0)
    PaperButton.grid(row=7,column=0)
    ScissorsButton.grid(row=8,column=0)
    
def incScore():
    global computerScore
    global myScore
    global myChoice
    global computerChoice
    computerChoice=random.randint(1,3)
    s="Computer choice is: "+options[computerChoice]
    tkComputerChoice.set(s)     
    #Check choice and inc score
    if((computerChoice-myChoice)%3==1):
        computerScore=computerScore+1
        s="Computer's Score: "+str(computerScore)
        tkComputerScore.set(s)
    elif(myChoice==computerChoice):
        print("No one scores\nComputer Score: ",computerScore,"\nYour Score: ",myScore)   
    else:
        myScore=myScore+1
        s="Your Score: "+str(myScore)
        tkMyScore.set(s)
        
    
import random
import sys

from functools import partial
import tkinter as tk

root = tk.Tk()
w = tk.Label(root,text="Welcome to Rock, Paper and Scissors Game!")
w.grid(row=0,columnspan=3, rowspan=2)

LengthLabel=tk.Label(root, text="Game Length:")
Games7Button= tk.Button(root,text="7 Rounds",command= partial(setNumberOfGames,7))
Games5Button= tk.Button(root,text="5 Rounds",command= partial(setNumberOfGames,5))
Games3Button= tk.Button(root,text="3 Rounds",command= partial(setNumberOfGames,3))

var = tk.IntVar()
RadioLabel=tk.Label(root, text="Mode:",justify=tk.LEFT)
RadioLabel.grid(sticky=tk.E)
R1 = tk.Radiobutton(root, text="Limited", variable=var, value=1,
                  command=lambda: (LengthLabel.grid(row=3,columnspan=2,sticky=tk.E),Games7Button.grid(row=4,column=0),Games5Button.grid(row=4,column=1),Games3Button.grid(row=4,column=2)))
R1.grid(row=2,column=1)

R2 = tk.Radiobutton(root, text="Unlimited", variable=var, value=2,
                  command=lambda: (LengthLabel.grid_forget(),Games7Button.grid_forget(),Games5Button.grid_forget(),Games3Button.grid_forget(), setNumberOfGames(sys.maxsize)))
R2.grid(row=2,column=2)

ChoiceLabel=tk.Label(root, text="Select your Choice:",justify=tk.LEFT)

RockButton = tk.Button(root,bg='SlateGray4' ,text ="Rock",command = partial(setMyChoice,1))

PaperButton = tk.Button(root,bg='khaki' ,text ="Paper",command = partial(setMyChoice,2))

ScissorsButton = tk.Button(root,bg='cadetblue1', text ="Scissors",command = partial(setMyChoice,3))

EndButton = tk.Button(root,text='End Game',bg='tomato2',command = displaywinner)

tkComputerChoice=tk.StringVar()
tkMyChoice=tk.StringVar()

tkComputerScore=tk.StringVar()
tkComputerScore.set("Computer's Score: 0")
tkMyScore=tk.StringVar()
tkMyScore.set("Your Score: 0")

tkWinner=tk.StringVar()

# if(mode==2):
#     EndButton.grid(row=6,column=2,columnspan=2)

frame = tk.Frame(root,borderwidth=3,bg='lightgreen',relief=tk.RAISED)
frame.grid(row=9,columnspan=3,sticky=tk.W+tk.E)

count=tk.IntVar()
count.set(numberOfGames)
choiceLabel1=tk.Label(frame,bg='lightgreen',textvariable=tkComputerChoice,justify=tk.LEFT)
choiceLabel2=tk.Label(frame,bg='lightgreen',textvariable=tkMyChoice,justify=tk.LEFT)

scoreLabel1=tk.Label(frame,bg='lightgreen',textvariable=tkComputerScore,justify=tk.LEFT)
scoreLabel2=tk.Label(frame,bg='lightgreen',textvariable=tkMyScore,justify=tk.LEFT)

winLabel=tk.Label(frame,bg='lightgreen',textvariable=tkWinner)

choiceLabel1.grid(row=1,columnspan=3)
choiceLabel2.grid(row=2,columnspan=3)

scoreLabel1.grid(row=3,columnspan=3)
scoreLabel2.grid(row=4,columnspan=3)

winLabel.grid(row=5,columnspan=3)

root.mainloop()
