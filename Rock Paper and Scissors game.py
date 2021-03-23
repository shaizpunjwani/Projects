from tkinter.messagebox import showinfo 
from tkinter import Tk,Label,Entry,Button
import random

def player_input():
    #fetching the entry box choice
    player=ent.get()
    return player

def Game():
    #calling the player function
    p=player_input()
    #setting a list where we can apply random module and get random option from it
    options=['rock','paper','scissors']
    if p.lower() not in options:
        showinfo(message='Enter correct choice')
        return -1
    computer=random.choice(options)

    #--------------------------------------
        
    #here we setted all the conditions in the game and displayed it in the showinfo message in our gui
    if computer==p:
        showinfo(message='Tie')
    
    elif computer=="rock":
        if p =='paper':
            showinfo(message='You Won')
        else:
            showinfo(message=('you Lose'))

    elif computer=="paper":
        if p=='scissors':
            showinfo(message='You Won')
        else:
            showinfo(message=('you Lose'))
        
    elif computer=='scissors':
            if p=='rock':
                showinfo(message='You Won')
            else:
                showinfo(message='You lose')


#----------------------------------------------

#here we set our gui

root=Tk()
label=Label(master=root,text='ROCK PAPER AND SCISSORS', font=('Helvetica', 30, 'bold italic'))
label.place(x=50,y=50)
ent=Entry(root)
label1=Label(root,text='ENTER YOUR CHOICE ROCK, PAPER OR SCISSOR')
ent.place(x=300,y=200)
label1.place(x=0,y=200)
button=Button(root,text="Submit",command=Game)
button.place(x=500,y=200)
root.mainloop()


