"""
Blackjack Card Game
"""
import random

class Card:
    def __init__(self, face, suit):
        self.face = face
        self.suit = suit

    def __repr__(self):
        return f"({self.face}, {self.suit})"

    def getValue(self): # Test Driving Development
        if self.face.isdigit():
            return int(self.face)
        pictured = {"ACE":1, "JACK":11, "QUEEN":12, "KING":13}
        return pictured[self.face]

class BlackjackCard(Card):
    def getValue(self): # override getValue() from superclass
        if self.face.isdigit():
            return int(self.face)
        pictured = {"ACE":11, "JACK":10, "QUEEN":10, "KING":10}
        return pictured[self.face]

class Deck:
    FACES = ('ACE', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'JACK', 'QUEEN', 'KING')
    SUITS = ('SPADES', 'CLUBS', 'DIAMONDS', 'HEARTS')
    def __init__(self):
        # self.stackOfCards = [BlackjackCard(face, suit)for face in Deck.FACES for suit in Deck.SUITS]
        # regular way to generate stack of cards
        # self.stackOfCards = []
        # for f in Deck.FACES:
        #     for s in Deck.SUITS:
        #         card = BlackjackCard(f, s)
        #         self.stackOfCards.append(card)
        self.currentIndex = 51

    def shuffle(self):
        random.shuffle(self.stackOfCards)

    def nextCard(self):
        card = self.stackOfCards[self.currentIndex]
        self.currentIndex -= 1
        return card

if __name__ == '__main__':
    heartsA = Card("ACE", "HEARTS")
    print(heartsA)
