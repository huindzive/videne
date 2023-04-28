#Lietotne ļauj ievadīt dzimšanas datus un programma dod iespēju parādīt vecumu gados, dienās vai sekundēs.

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
import random
import time

date = [28,4,2023]
vecums = [0,0,0]
rezultats = 0

window = Tk()
window.geometry("500x500")
window.title("Gadi")
window.config(background="white")

def submit(funkcija):
    global date
    global vecums
    global rezultats
    if gads.get() != "" and menesis.get() != "" and diena.get() != "" :
        vecums[2] = int(gads.get())
        vecums[1] = int(menesis.get())
        vecums[0] = int(diena.get())
        if funkcija == 'gadi':
            print('gadi')
            if date[1] > vecums[1]:
                rezultats = date[2] - vecums[2]
                readout.config(text=str(rezultats) +" " +funkcija)
            else:
                rezultats = date[2] - vecums[2]+1
                readout.config(text=str(rezultats) +" " +funkcija)
        elif funkcija == 'stundas':
            if date[1] > vecums[1]:
                rezultats = ((date[2] - vecums[2]) * 365*24) + abs((date[1] - vecums[1]) * 30*24)+abs(date[0] - vecums[0] * 24)
                readout.config(text=rezultats)
            else:
                rezultats = ((date[2] - vecums[2]+1) * 365*24) + abs((date[1] - vecums[1]) * 30*24)+abs(date[0] - vecums[0] * 24)
                readout.config(text=str(rezultats) +" " +funkcija)

        else:
            print("sekundes")
            if date[1] > vecums[1]:
                rezultats = ((date[2] - vecums[2]) * 365*24*3600) + abs((date[1] - vecums[1]) * 30*24*3600)+ abs(date[0] - vecums[0] * 24*3600)
                readout.config(text=str(rezultats) +" " +funkcija)
            else:
                rezultats = ((date[2] - vecums[2]+1) * 365*24*3600) + abs((date[1] - vecums[1]) * 30*24*3600)+abs(date[0] - vecums[0] * 24*3600)
                readout.config(text=str(rezultats) +" " +funkcija)
    else:
        messagebox.showinfo("error",'nav ievadīti visi datumi')

    print(vecums)

gads = Entry(window,
            font=("Visby",20),
            fg="Black",
            background="white")

menesis = Entry(window,
            font=("Visby",20),
            fg="Black",
            background="white")

diena = Entry(window,
            font=("Visby",20),
            fg="Black",
            background="white")

nDiena = Label(
            font=("Visby",13, "bold"),
            text="Diena",
            background="#FFFFFF",
            relief=FLAT)

nMenesis = Label(
            font=("Visby",13, "bold"),
            text="Menesis",
            background="#FFFFFF",
            relief=FLAT)

nGads = Label(
            font=("Visby",13, "bold"),
            text="Gads",
            background="#FFFFFF",
            relief=FLAT)

readout = Label(
            font=("Visby",13, "bold"),
            text="",
            background="#FFFFFF",
            relief=FLAT)

Gados = Button(window,
                font=("Visby",13, "bold"),
                text="Gados",
                background="green",
                activebackground="#94a0a8",
                command=lambda:submit("gadi"))

Stundas = Button(window,
                font=("Visby",13, "bold"),
                text="Stundās",
                background="yellow",
                activebackground="#94a0a8",
                command=lambda:submit("stundas"))

Sekundes = Button(window,
                font=("Visby",13, "bold"),
                text="Sekundēs",
                background="red",
                activebackground="#94a0a8",
                command=lambda:submit("sekundes"))


gads.place(x=100,y=40)
menesis.place(x=100,y=140)
diena.place(x=100,y=240)
nMenesis.place(x=20,y=142)
nDiena.place(x=20,y=242)
nGads.place(x=20,y=42)

Gados.place(x=20,y=350)
Stundas.place(x=120,y=350)
Sekundes.place(x=220,y=350)
readout.place(x=150,y=450)

window.mainloop()