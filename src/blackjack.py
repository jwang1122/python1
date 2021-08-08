"""
Blackjack Card Game
"""
import random

class Card:
    def __init__(self, face, suit):
        self.face = face
        self.suit = suit

    def __repr__(self): # this dunder function return a string to represent this object(card).
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
        self.winCount = 0 # also add this attribute to Dealer

    def win(self):
        self.winCount += 1

    def __repr__(self):
        return self.name

    def addCardToHand(self, card):
        self.hand.append(card)
    
    def cleanHand(self):
        self.hand.clear()

    def getHandSize(self):
        return len(self.hand)

    def showHand(self):
        return f"{self.name}: {self.hand}:{self.getHandValue()}:{self.winCount}"

    def getHandValue(self):
        value = 0
        for card in self.hand:
            value += card.getValue()
        if value > 21 and self.hasAce(): # A=11,
            value -= 10 # change A=1
        return value

    def hasAce(self):
        for card in self.hand:
            if card.face == 'A':
                return True
        return False # return False till check every card in hand

    def hit(self):
        value = self.getHandValue()
        if value >=20:
            return False
        moreCard = input(self.name + ", do you want another card? (y/n) ")
        if moreCard=='y':
            return True
        return False

class Dealer(Player):
    def __init__(self):
        self.name = "Dealer"
        self.hand = []
        self.deck = Deck()
        self.winCount = 0

    def hit(self):
        value = self.getHandValue()
        if value < 17:
            return True
        return False

    def shuffle(self):
        self.deck.shuffle()

    def deal(self):
        return self.deck.nextCard()

    def showHand(self, faceUp):
        if not faceUp:
            return f"{self.name}: [{self.hand[0]}, HIDDEN]"
        return super().showHand()

class Game:
    def __init__(self, player):
        self.player = player
        self.dealer = Dealer()
        self.dealer.shuffle()

    def dealCards(self):
        self.player.addCardToHand(self.dealer.deal())
        self.dealer.addCardToHand(self.dealer.deal())
        self.player.addCardToHand(self.dealer.deal())
        self.dealer.addCardToHand(self.dealer.deal())
        print(self.player.showHand())
        print(self.dealer.showHand(False))

    def showResult(self):
        print(self.player.showHand())
        print(self.dealer.showHand(True))

    def cleanHand(self):
        self.player.cleanHand()
        self.dealer.cleanHand()

    def hit(self):
        while self.player.hit():
            self.player.addCardToHand(self.dealer.deal())
            print(self.player.showHand())
        while self.dealer.hit():
            self.dealer.addCardToHand(self.dealer.deal())

    def play(self):
        while(True):
            self.dealCards()
            self.hit()
            determineWinner(self.dealer, self.player)
            self.showResult()
            moreGame = input("Would you like to play another game? (y/n) ")
            if moreGame=='n':
                break
            self.cleanHand()
        print("Game Over!")

def determineWinner(dealer, player):
    dealerTotal = dealer.getHandValue()
    playerTotal = player.getHandValue()
    if playerTotal>21:
        dealer.win()
    elif dealerTotal>21:
        player.win()
    elif playerTotal==dealerTotal:
        pass
    elif playerTotal > dealerTotal:
        player.win()
    else:
        dealer.win()

if __name__ == '__main__':
    KaydentheDude = Player("KaydentheDude")
    game = Game(KaydentheDude)
    game.play()
