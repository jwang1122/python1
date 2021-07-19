"""
create Card class for the Blackjack Game
"""
from enum import Enum

class Card:
    Face = Enum('Face',('A','2','3','4','5','6','7','8','9','10','J','Q','K'))
    Suit = Enum('Suit',('Diamonds','Clubs','Spades', 'Hearts')) # Suit is class level attribute

    def __init__(self, face, suit):
        self.face = face
        self.suit = suit

    def __repr__(self):
        return f"({self.face.name}, {self.suit.name})"

    def __add__(self, other): # __add__() override + arithmetic operator
        return self.getValue() + other.getValue()

    def __eq__(self, other): # __eq__() override == comparison operator
        return self.getValue() == other.getValue()

    def __gt__(self, other):
        return self.getValue() > other.getValue()

    def __lt__(self, other):
        return self.getValue() < other.getValue()

    def getValue(self):
        pictured = {'A':11, 'J':10, 'Q':10, 'K':10}
        if self.face.name.isdigit():
            return self.face.value
        return pictured[self.face.name]

if __name__ == '__main__':
    heartsJ = Card(Card.Face.J, Card.Suit.Hearts) # heartsJ is instance of Card class
    print(heartsJ)
    print(heartsJ.getValue())
    diamondsA = Card(Card.Face.A, Card.Suit.Diamonds)
    print(diamondsA)
    print(diamondsA.getValue())
    x = heartsJ + diamondsA # override + operator
    print(x)
    diamondsK = Card(Card.Face.K, Card.Suit.Diamonds)
    print(diamondsK)

    print(diamondsK==heartsJ)
    print(diamondsA>heartsJ)
    print(diamondsA<heartsJ)


    # x = heartsJ.getValue # I am assigning function to x, to make the x as a function
    # print(type(x))
    # print(x()) # now I am calling on the function x