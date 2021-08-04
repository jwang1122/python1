"""
Blackjack Card Game

Game Rules:
https://bicyclecards.com/how-to-play/blackjack/

"""
import random

class Card:
    """
    Base class for blackjack card game.

    it has two attributes, face and suit, and a getValue() function which return the face value of the card.
    where A=1, 2=2, ..., J=11, Q=12, K=13
    """
    def __init__(self, face, suit):
        """
        Sample code for create Card instance:

        card = Card("A", "DIAMONDS")

        here is all SUITS "SPADES, DIAMONDS, CLUBS, HEARTS".
        """
        self.face = face
        self.suit = suit

    def __repr__(self): # this dunder function return a string to represent this object(card).
        """
        return a string to represent the card, for intance, (A, HEARTS).
        """
        return f"({self.face}, {self.suit})"

    def getValue(self): # Test Driving Development
        """
        use dictionary to get value of A, J, Q, K
        """
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
        for card in self.hand: #A,Q,A,Q=42
            value += card.getValue()
        count = self.countAce()
        while value > 21 and count>0: # A=11,
            value -= 10 # change A=1
            count -= 1
        return value # 22

    def countAce(self):
        count = 0
        for card in self.hand:
            if card.face == 'A':
                count += 1
        return count # return number of Ace in hand

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
    def __init__(self, playerList):
        self.playerList = playerList
        self.dealer = Dealer()
        self.dealer.shuffle()

    def dealCards(self):
        for player in self.playerList: # first round for all player
            player.addCardToHand(self.dealer.deal())
        self.dealer.addCardToHand(self.dealer.deal())
        for player in self.playerList: # second round for all player
            player.addCardToHand(self.dealer.deal())
            print(player.showHand())
        self.dealer.addCardToHand(self.dealer.deal())
        print(self.dealer.showHand(False))

    def showResult(self):
        for player in self.playerList:
            print(player.msg)
            print(player.showHand())
        print(self.dealer.showHand(True))

    def cleanHand(self):
        for player in self.playerList:
            player.cleanHand()
        self.dealer.cleanHand()

    def hit(self):
        for player in self.playerList:
            while player.hit():
                player.addCardToHand(self.dealer.deal())
                print(player.showHand())
        while self.dealer.hit():
            self.dealer.addCardToHand(self.dealer.deal())

    def play(self, winner):
        while(True):
            self.dealCards()
            self.hit()
            for player in self.playerList:
                winner(self.dealer, player)
            self.showResult()
            moreGame = input("Would you like to play another game? (y/n) ")
            if moreGame=='n':
                break
            self.cleanHand()
        print("Game Over!")

# if without else: each function takes a single responsibility
def winner(dealer, player):
    dealer.total = dealer.getHandValue() # dynamically create an attribute in dealer
    player.total = player.getHandValue() # add attribute total to player
    if player.total > 21:
        player.msg = f"Dealer win, {player.name} busted!"
        return dealer.win()
    return dealerBusted(dealer, player)   

def dealerBusted(dealer, player):
    if dealer.total > 21:
        player.msg = f"{player.name} wins, dealer busted!"
        return player.win()
    return tiedUp(dealer, player)

def tiedUp(dealer, player):
    if dealer.total==player.total:
        player.msg = "Tied up, no body wins."
        return
    return playerLarge(dealer, player)

def playerLarge(dealer, player):
    if player.total > dealer.total:
        player.msg = f"{player.name} wins, {player.name} has large hand."
        return player.win()
    player.msg = "Dealer wins, dealer has large hand."
    return dealer.win()

def determineWinner(dealer, player):
    dealerTotal = dealer.getHandValue()
    playerTotal = player.getHandValue()
    player.msg = ""
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

def buildPlayerList():
    playerList = []
    while True:
        morePlayer = input("Player? (y/n)")
        if morePlayer=='n':
            break
        player = Player(getName(playerList))
        playerList.append(player)
    return playerList

def getName(playerList):
    while True:
        name = input("enter a name: ")
        if contains(name, playerList):
            print(f"the '{name}' is aready taken.")
        else: break
    return name

def contains(name, playerList):
    for player in playerList:
        if name == player.name:
            return True
    return False

if __name__ == '__main__':
    game = Game(buildPlayerList())
    game.play(winner) # pass function to play function
