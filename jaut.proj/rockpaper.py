from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
import random
import time

# window
window = Tk()
window.geometry("500x500")
window.title("Akmens papīrs")
window.config(background="white")

score = [0,0,0]
health = 3

def display(player,computer):
    movesLabel.config(text=player+' vs '+computer)
    healthLabel.config(text = "health: "+str(health))
def akmensskeres(player):
    global score
    global health

    movesLabel.config(text=player + " vs ")
    
    moves = ['akmens','skeres','papirs']
    computer = random.choice(moves)

    if player == computer:
        score[1] += 1
    elif (player == "akmens" and computer == 'skeres') or (player == "skeres" and computer == 'papirs') or (player == "papirs" and computer == 'akmens'):
        score[0] += 1
    else:
        score[2] += 1
        health-=1

    movesLabel.after(1000,lambda: display(player,computer))

    if health == 0:
        messagebox.showinfo("Error","Jou Lost \n "+"score: "+str(score[0])+ " - "+str(score[1])+' - '+str(score[2]))
        window.destroy()


    

# buttons
akmens = Button(window,
                font=("Visby",13, "bold"),
                text="akmens",
                background="#FFFFFF",
                activebackground="#94a0a8",
                command=lambda:akmensskeres("akmens"))

skeres = Button(window,
                font=("Visby",13, "bold"),
                text="skeres",
                background="#FFFFFF",
                activebackground="#94a0a8",
                command=lambda:akmensskeres("skeres"))

papirs = Button(window,
                font=("Visby",13, "bold"),
                text="papirs",
                background="#FFFFFF",
                activebackground="#94a0a8",
                command=lambda:akmensskeres("papirs"))

akmens.place(x=40,y=40)
skeres.place(x=140,y=40)
papirs.place(x=240,y=40)

movesLabel = Label(
            font=("Visby",13, "bold"),
            text="",
            background="#FFFFFF",
            relief=FLAT)

movesLabel.place(x = 50,y=100)

healthLabel = Label(
            font=("Visby",13, "bold"),
            text="health = 3",
            background="#FFFFFF",
            relief=FLAT)

healthLabel.place(x = 100,y=450)

window.mainloop()