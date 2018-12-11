from tkinter import *
import tkinter as tk
import tkinter.messagebox as tkMessageBox
import sqlite3
import tkinter.ttk as ttk
import time

root = Tk()
root.title("Product Scheduler")
screen_width = root.winfo_screenmmwidth()
screen_height = root.winfo_screenmmheight()
width = 900
height = 500
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)

root.geometry('%dx%d+%d+%d' % (width,height,x,y))
root.resizable(0,0)

#==================================VARIABLES==========================================
JOBNUMBER = StringVar()
RECIPECODE = StringVar()
DESCRIPTION = StringVar()

#==================================METHODS==========================================
def Database():
    """Create the database, else open it"""
    global conn, cursor
    conn = sqlite3.connect('sched_prod.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS 'recipes'(rec_code TEXT)")

def create():
    if JOBNUMBER.get() == "" :
        txt_result.config(text="Please enter the recipe code", fg="red")
    else:
        testentry = str(JOBNUMBER.get())
        Database()
        print(len((testentry,)))
        cursor.execute("INSERT INTO 'recipes' (rec_code)VALUES(?)",(testentry,))
        conn.commit()
        JOBNUMBER.set("")

        cursor.close()
        conn.close()
        txt_result.config(text="Schedule DB created!", fg="green")


#==================================FRAME==============================================
TopFrame = Frame(root, width=900, height=50, bd=14, relief="raise")
TopFrame.pack(side=TOP)

LeftFrame = Frame(root, width=300, height=500, bd=8, relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(root, width=600, height=500, bd=8, relief="raise")
RightFrame.pack(side=RIGHT)

Forms = Frame(LeftFrame,width=300, height=450)
Forms.pack(side=TOP)

Buttons = Frame(LeftFrame,width=300, height = 100, bd=14,relief='raise')
Buttons.pack(side=(TOP))

#========================LABELS WIDGETS===============================================
txt_title = Label(TopFrame, width = 900, font=('arial',24),text = 'Insert Jobs Into Schedule')
txt_title.pack()

txt_jobNum = Label(Forms, text="Job Number: ", font=('arial',16),bd=15)
txt_jobNum.grid(row=0, stick='e')


txt_result = Label(Buttons)
txt_result.pack(side=TOP)
#======================ENTRY WIDGETS==================================================
entry_jobNum = Entry(Forms,textvariable=JOBNUMBER,width=30)
entry_jobNum.grid(row=0,column=1)

#==================================BUTTONS WIDGETS===================================
btn_start = Button(Buttons, width=10, text="Start", command=create)
btn_start.pack(side=LEFT)




#===============start the app=========================================================
if __name__ == '__main__':
    root.mainloop()