from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
import sqlite3

# Create table
conn = sqlite3.connect("datasheet.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS datasheet (id INTEGER PRIMARY KEY, type VARCHAR, model VARCHAR, price FLOAT)")
conn.commit()

# Display data in Tree widget
def display():
    tree.delete(*tree.get_children())
    cursor.execute("SELECT * FROM datasheet")
    parts = cursor.fetchall()
    
    for part in parts:
        tree.insert('', 'end', text="2", values=(part[0], part[1], part[2], part[3]))
        

# Submit
def submit():
    conn = sqlite3.connect("datasheet.db")
    cursor = conn.cursor()
    if type.get() != "" and name.get() != "" and price.get() != "":
        cursor.execute("INSERT INTO datasheet (type, model, price) VALUES (?, ?, ?)", (type.get(), name.get(), float(price.get())))
    conn.commit()
    display()

# Delete item
def delete():
    treeIndex = tree.focus()
    id = tree.item(treeIndex)["values"][0] # focus atgriež indeksu, kuru izmanto, lai dabūtu konkrēto item
    cursor.execute("DELETE FROM datasheet WHERE id = ?", str(id))
    conn.commit()
    display()


# Window configuration
window = Tk()

window.geometry("800x400")
window.title("Datora sastavdalas")
window.config(background="white")

# Title
name = Label(window,
             font=("Visby",20, "bold"),
             text="Datora sastāvdaļas",
             background="#94a0a8",
             relief=FLAT)

name.place(x=10, y =10)

# Entry Boxes
type = Entry(window,
             font=("Visby",20),
             fg="Black",
             background="white")

type.place(x=10, y=60)

name = Entry(window,
             font=("Visby",20),
             fg="Black",
             background="white")

name.place(x=10, y=100)

price = Entry(window,
             font=("Visby",20),
             fg="Black",
             background="white")

price.place(x=10, y=140)

# Submit Button
submitb = Button(window,
                font=("Visby",13, "bold"),
                text="submit",
                background="#94a0a8",
                activebackground="#94a0a8",
                command=submit)

submitb.place(x=330, y= 140)

tree = ttk.Treeview(window, column=("c1", "c2", "c3", "c4"), show='headings', height=8)

tree.column("# 1", anchor=CENTER)
tree.heading("# 1", text="ID")
tree.column("# 2", anchor=CENTER)
tree.heading("# 2", text="Type")
tree.column("# 3", anchor=CENTER)
tree.heading("# 3", text="Name")
tree.column("# 4", anchor=CENTER)
tree.heading("# 4", text="Price")

tree.pack(side=BOTTOM)

# Delete button from list
ldelete = Button(window,
                 font=("Visby",13, "bold"),
                 text="delete",
                 background="Red",
                 activebackground="Red",
                 command=delete)

ldelete.place(x=450,y=140)

edit = Button(window,
                 font=("Visby",13, "bold"),
                 text="edit",
                 background="White",
                 activebackground="White",
                 command=delete)

edit.place(x=550,y=140)


# Program executer
display()
window.mainloop()
conn.close()