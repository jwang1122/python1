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
        self.stackOfCards = [BlackjackCard(face, suit) for face in Deck.FACES for suit in Deck.SUITS]
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
        self.winCount = 0

    def __repr__(self):
        return self.name

    def addCardToHand(self, card):
        self.hand.append(card)
    
    def cleanHand(self):
        self.hand.clear()

    def getHandSize(self):
        return len(self.hand)

    def showHand(self):
        return f"{self.name}: {self.hand}"

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

    def win(self):
        self.winCount += 1

    def showHand(self):
        return f"{self.name}:{self.hand}:{self.getHandValue()}:{self.winCount}"

class Dealer(Player):
    def __init__(self):
        self.name = "Dealer"
        self.hand = []
        self.deck = Deck()
        self.winCount = 0

    def shuffle(self):
        self.deck.shuffle()

    def hit(self):
        value = self.getHandValue()
        if value < 17:
            return True
        return False

    def deal(self):
        return self.deck.nextCard()
    
    def showHand(self, faceUp):
        if not faceUp:
            return f"{self.name}:[{self.hand[0]}, HIDDEN]"
        return super().showHand()
        
class Game:
    def __init__(self, player):
        self.player = player
        self.dealer = Dealer()
        self.dealer.shuffle()

    def play(self, whoWin):
        while(True):
            self.player.addCardToHand(self.dealer.deal())
            self.dealer.addCardToHand(self.dealer.deal())
            self.player.addCardToHand(self.dealer.deal())
            self.dealer.addCardToHand(self.dealer.deal())
            print(self.player.showHand())
            print(self.dealer.showHand(False))

            while self.player.hit():
                self.player.addCardToHand(self.dealer.deal())
                print(self.player.showHand())
            while self.dealer.hit():
                self.dealer.addCardToHand(self.dealer.deal())
            print(whoWin(self.dealer, self.player))
            print(self.player.showHand())
            print(self.dealer.showHand(True))

            moreGame = input(f"{self.dealer}, do you want to play again? (y/n) ")
            if moreGame == 'n':
                break
            print()
            self.dealer.cleanHand()
            self.player.cleanHand()

# if without else, single responsibility
def winner1(dealer, player):
    dealerTotal = dealer.getHandValue()
    playerTotal = player.getHandValue()
    if playerTotal > 21:
        dealer.win()
        return "Dealer win, player busted!"
    return dealerBust(dealer, player, dealerTotal, playerTotal)

def dealerBust(dealer, player, dealerTotal, playerTotal):
    if dealerTotal > 21:
        player.win()
        return "Player win, dealer busted!"
    return tie(dealer, player, dealerTotal, playerTotal)

def tie(dealer, player, dealerTotal, playerTotal):
    if dealerTotal == playerTotal:
        return "Tied up."
    return playerGreater(dealer, player, dealerTotal, playerTotal)

def playerGreater(dealer, player, dealerTotal, playerTotal):
    if dealerTotal < playerTotal:
        player.win()
        return "Player win, player has greater hand."
    dealer.win()
    return "Dealer win, dealer has greater hand."
        
def winner(dealer, player):
    dealerTotal = dealer.getHandValue()
    playerTotal = player.getHandValue()
    if playerTotal > 21:
        dealer.win()
        result = "Dealer win, player busted!"
    elif dealerTotal > 21:
        player.win()
        result = "Player win, dealer busted!"
    elif playerTotal==dealerTotal:
        result = "Tied up."
    elif playerTotal > dealerTotal:
        player.win()
        result = "Player win, player has greater hand."
    else:
        dealer.win()
        result = "Dealer win, dealer has greater hand."
    return result

def determineWinner(dealer, player):
    dealerTotal = dealer.getHandValue()
    playerTotal = player.getHandValue()
    if playerTotal>21 and dealerTotal<=21:
        dealer.win()
        result = "\nDealer wins - Player busted!"
    elif playerTotal<=21 and dealerTotal>21:
        player.win()
        result = "\nPlayer wins - Dealer busted!"
    elif playerTotal>21 and dealerTotal>21:
        dealer.win()
        result = "\nBoth players bust! Dealer win."
    elif playerTotal<dealerTotal:
        dealer.win()
        result = "\nDealer has bigger hand value!"
    elif playerTotal == dealerTotal :
        result = "\nThe player and dealer have same hand value."
    else:
        player.win()
        result = "\nPlayer has bigger hand value!"
    return result


if __name__ == '__main__':
    john = Player("John")
    game = Game(john)
    game.play(winner1)
    
    # heartsA = Card("A", "HEARTS")
    # print(heartsA)
    # dealer = Dealer()
    # heartsA = BlackjackCard("A", "HEARTS")
    # diamonds4 = BlackjackCard("4", "DIAMONDS")
    # dealer.addCardToHand(heartsA)
    # dealer.addCardToHand(diamonds4)
    # dealer.showHand(False)
    # dealer.showHand(True)
    # Dealer:[(A, HEARTS), HIDDEN]
    # Dealer:[(A, HEARTS), (4, DIAMONDS)]:15:0