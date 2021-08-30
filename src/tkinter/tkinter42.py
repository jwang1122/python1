from tkinter import *

def test():
    diamond5 = PhotoImage(file = "images/diamond5.gif")
    lbl1 = Label(root, image=diamond5)
    lbl1.configure(image=diamond5)
    lbl1.image = diamond5
    lbl1.place(x=40, y=10)

root = Tk()
root.geometry('1010x740')

heartQ = PhotoImage(file="images/heartQ.gif")
lbl1 = Label(root, image=heartQ)
lbl1.place(x = 10, y = 10)

Button(root, text="Deal card", command=test).pack()

root.mainloop()