"""
create Card class for the Blackjack Game
"""
from enum import Enum

class Card:
    Face = Enum('Face',('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King'))
    Suit = Enum('Suit',('Diamonds', 'Clubs', 'Spades', 'Hearts'))
    
    def __init__(self, face, suit):
        self.face = face
        self.suit = suit

    def __repr__(self):
        return f"({self.face.name}, {self.suit.name})"

    def __add__(self, other):
        return self.getValue() + other.getValue()

    def getValue(self):
        pictured = {'Ace':11, 'Jack':10, 'Queen':10, 'King':10}
        if self.face.name.isdigit():
            return self.face.value
        return pictured[self.face.name]

if __name__ == '__main__':
    heartsJ = Card(Card.Face.Jack, Card.Suit.Hearts)
    print(heartsJ.getValue())
    print(heartsJ)
    diamondsA = Card(Card.Face.Ace, Card.Suit.Diamonds)
    print(diamondsA.getValue())
    print(diamondsA)
    x = heartsJ + diamondsA # override + operator
    print(x)
    
    # x = heartsJ.getValue # I am assigning function to 'x', to make 'x' a function
    # print(type(x))
    # print(x()) # now I am calling the function 'x'
