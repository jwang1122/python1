"""
Display image on window
"""
from tkinter import *

def deal():
    diamond5 = PhotoImage(file = "images/diamond5.gif")
    lbl1 = Label(root, image=diamond5)
    lbl1.configure(image=diamond5)
    lbl1.image = diamond5
    lbl1.place(x=40, y=10)

root = Tk()
root.geometry('1010x740+500+200') # where the (500, 300) is top-left cornor of the window

heartQ = PhotoImage(file="images/heartQ.gif")
lbl1 = Label(root, image=heartQ)
lbl1.place(x = 10, y = 10)

Button(root, text="Deal card", command=deal).pack()

root.mainloop()