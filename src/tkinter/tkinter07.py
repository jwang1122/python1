"""
Using Combox (Dropdown)
"""

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Combox")
root.geometry("600x300")
myVariable = tk.StringVar()
mybox = ttk.Combobox(root, textvariable=myVariable, values=['JavaScript','Java', 'Python','C++', 'C#'])

mybox.grid(row = 0, column=0)

def change(event):
    print(myVariable.get())

mybox.bind("<<ComboboxSelected>>", func=change)

tk.mainloop()