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
        pictured = {"A":1, "J":11, "Q":12, "K":13}
        return pictured[self.face]

class BlackjackCard(Card):
    def getValue(self): # override getValue() from superclass
        if self.face.isdigit():
            return int(self.face)
        pictured = {"A":11, "J":10, "Q":10, "K":10}
        return pictured[self.face]

class Deck:
    FACES = ('A','2','3','4','5','6','7','8','9','10','J','Q','K') # class level attribute
    SUITS = ('SPADES','CLUBS','DIAMONDS','HEARTS')
    def __init__(self):
        # more powerful way to generate stack of cards
        self.stackOfCards = [BlackjackCard(face, suit) for face in Deck.FACES for suit in Deck.SUITS]
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
        if self.currentIndex==0:
            self.shuffle()
            self.currentIndex = 51
        return card

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def addCardToHand(self, card):
        self.hand.append(card)
    
    def cleanHand(self):
        self.hand.clear()

    def getHandSize(self):
        return len(self.hand)

    def showHand(self):
        myHand = f"{self.name}: {self.hand}"
        return myHand

    def getHandValue(self):
        value = 0
        for card in self.hand:
            value += card.getValue()
        return value

if __name__ == '__main__':
    heartsA = Card("A", "HEARTS")
    print(heartsA)