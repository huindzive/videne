from tkinter import*
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox

root = Tk()
root.title("Python: Simple CRUD Applition")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 900
height = 500
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(0, 0)

#==================================METHODS============================================
def Database():
    global conn, cursor
    conn = sqlite3.connect('pythontut.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, type VARCHAR, model VARCHAR, price FLOAT)")
    
def Create():
    if  TYPE.get() == "" or MODEL.get() == "" or PRICE.get() == "":
        txt_result.config(text="Please complete the required field!", fg="red")
    else:
        Database()
        cursor.execute("INSERT INTO `member` (type, model, price) VALUES(?, ?, ?)", (str(TYPE.get()), str(MODEL.get()), str(PRICE.get())))
        conn.commit()
        TYPE.set("")
        MODEL.set("")
        PRICE.set("")
        cursor.close()
        conn.close()
        txt_result.config(text="Created a data!", fg="green")

def Read():
    tree.delete(*tree.get_children())
    Database()
    cursor.execute("SELECT * FROM `member` ORDER BY `type` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data[1], data[2], data[3]))
    cursor.close()
    conn.close()
    txt_result.config(text="Successfully read the data from database", fg="black")
    
def Exit():
    result = tkMessageBox.askquestion('Python: Simple CRUD Applition', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()

#==================================VARIABLES==========================================
TYPE = StringVar()
MODEL = StringVar()
PRICE = DoubleVar()

#==================================FRAME==============================================
Top = Frame(root, width=900, height=50, bd=8, relief="raise")
Top.pack(side=TOP)
Left = Frame(root, width=300, height=500, bd=8, relief="raise")
Left.pack(side=LEFT)
Right = Frame(root, width=600, height=500, bd=8, relief="raise")
Right.pack(side=RIGHT)
Forms = Frame(Left, width=300, height=450)
Forms.pack(side=TOP)
Buttons = Frame(Left, width=300, height=100, bd=8, relief="raise")
Buttons.pack(side=BOTTOM)
RadioGroup = Frame(Forms)


#==================================LABEL WIDGET=======================================
txt_title = Label(Top, width=900, font=('arial', 24), text = "Python: Simple CRUD Application")
txt_title.pack()
txt_type = Label(Forms, text="type: ", font=('arial', 16), bd=15)
txt_type.grid(row=0, stick="e")
txt_model = Label(Forms, text="model", font=('arial', 16), bd=15)
txt_model.grid(row=1, stick="e")
txt_price = Label(Forms, text="price", font=('arial', 16), bd=15)
txt_price.grid(row=2, stick="e")
txt_result = Label(Buttons)
txt_result.pack(side=TOP)

#==================================ENTRY WIDGET=======================================
type = Entry(Forms, textvariable=TYPE, width=30)
type.grid(row=0, column=1)
model = Entry(Forms, textvariable=MODEL, width=30)
model.grid(row=1, column=1)
RadioGroup.grid(row=2, column=1)
price = Entry(Forms, textvariable=PRICE, width=30)
price.grid(row=3, column=1)

#==================================BUTTONS WIDGET=====================================
btn_create = Button(Buttons, width=10, text="Create", command=Create)
btn_create.pack(side=LEFT)
btn_read = Button(Buttons, width=10, text="Read", command=Read )
btn_read.pack(side=LEFT)
btn_update = Button(Buttons, width=10, text="Update", state=DISABLED)
btn_update.pack(side=LEFT)
btn_delete = Button(Buttons, width=10, text="Delete", state=DISABLED)
btn_delete.pack(side=LEFT)
btn_exit = Button(Buttons, width=10, text="Exit", command=Exit)
btn_exit.pack(side=LEFT)

#==================================LIST WIDGET========================================
scrollbary = Scrollbar(Right, orient=VERTICAL)
scrollbarx = Scrollbar(Right, orient=HORIZONTAL)
tree = ttk.Treeview(Right, columns=("type","model","price"), selectmode="extended", height=500, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('Firstname', text="Firstname", anchor=W)
tree.heading('Lastname', text="Lastname", anchor=W)
tree.heading('Gender', text="Gender", anchor=W)
tree.heading('Address', text="Address", anchor=W)
tree.heading('Username', text="Username", anchor=W)
tree.heading('Password', text="Password", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=80)
tree.column('#2', stretch=NO, minwidth=0, width=120)
tree.column('#3', stretch=NO, minwidth=0, width=80)
tree.pack()

#==================================INITIALIZATION=====================================
if __name__ == '__main__':
    root.mainloop()
