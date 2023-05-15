from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk

def output():
  x = type.get()
  label.config(text=x)

window = Tk()
window.geometry("400x400")
window.title("Piemers")
window.config(background="white")

type = Entry(window,
             font=("Visby",20),
             fg="Black",
             background="white")

type.place(x=10, y=60)

but = Button(window,
                font=("Visby",13, "bold"),
                text="Go",
                background="#94a0a8",
                activebackground="#94a0a8",
                command=output)

but.place(x=10, y=100)

label = Label(window,
             font=("Visby",15, "bold"),
             text="",
             background="white",
             relief=FLAT)

label.place(x=10, y =150)

window.mainloop()