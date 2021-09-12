from enum import Enum

class Suits(Enum):
    SPADES=1
    CLUBS=2
    DIAMONDS=3
    HEARTS=4

class Faces(bytes, Enum):
    def __new__(cls, value, label, score): # useful sample code for override __new__()
        obj = bytes.__new__(cls, [value])
        obj._value_ = value 
        obj.label = label
        obj.score = score
        return obj

    ACE= (1,"A", 11)
    TWO=(2,"2",2) 
    THREE=(3,"3",3)
    FOUR=(4,"4",4)
    FIVE=(5,"5",5)
    SIX=(6,"6",6)
    SEVEN=(7,"7",7)
    EIGHT=(8,"8",8)
    NINE=(9,"9",9)
    TEN=(10,"10",10)
    JACK=(11,"J",10)
    QUEEN=(12,"Q",10)
    KING=(13,"K",10)

class Card:
    def __init__(self, face, suit):
        self.face = face
        self.suit = suit

    def __repr__(self):
        return f"({self.face.label}, {self.suit.name})"

if __name__ == '__main__':
    for face in Faces:
        print(face)

    for suit in Suits:
        print(suit)
    
    diamondA = Card(Faces.ACE, Suits.DIAMONDS)
    print(diamondA)