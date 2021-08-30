import tkinter as tk
from PIL import Image
import random

class Card:
    suits = ['spades','clubs','diamonds','hearts']
    faces = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    
    def __init__(self, face, suit):
        self.face = face
        self.suit = suit

    def __repr__(self):
        return '('+self.face+', '+self.suit+')'

    def getImage(self):
        filename = 'images/' + self.suit + self.face+'.gif'
        image = tk.PhotoImage(file=filename)
        return image

def deal():
    pass

if __name__ == '__main__':
    card = Card('2','clubs')
    print(card)
    root = tk.Tk()
    root.geometry('1024x768')
    dealBtn = tk.Button(root, text="Deal Card", command=deal).place(x=5, y=5) 
    root.mainloop()
