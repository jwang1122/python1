import unittest
from src.blackjack import *

class TestCard(unittest.TestCase):
    heartsA = Card("A", "HEARTS")
    diamonds4 = Card("4", "DIAMONDS")
    clubsQ = Card("Q", "CLUBS")
    black_heartsA = BlackjackCard("A", "HEARTS")
    black_diamonds4 = BlackjackCard("4", "DIAMONDS")
    black_clubsQ = BlackjackCard("Q", "CLUBS")
    black_spades7 = BlackjackCard("7", "SPADES")

    roy = Player("roy") # class level attribute
    roy.addCardToHand(black_heartsA)
    roy.addCardToHand(black_clubsQ)
    dealer = Dealer() # create dealer instance

    def test_repr(self):
        self.assertEqual("Dealer", repr(self.dealer))

    def test_getCardValue(self):
        self.assertEqual(4, self.diamonds4.getValue())
        self.assertEqual(1, self.heartsA.getValue())
        self.assertEqual(12, self.clubsQ.getValue())

    def test_getBlackjackCardValue(self):
        self.assertEqual(4, self.black_diamonds4.getValue())
        self.assertEqual(11, self.black_heartsA.getValue())
        self.assertEqual(10, self.black_clubsQ.getValue())

    def test_numberOfCardsInDeck(self):
        deck = Deck()
        self.assertTrue(52, len(deck.stackOfCards))

    def test_firstCard(self):
        deck = Deck()
        self.assertEqual('(A, SPADES)', deck.stackOfCards[0].__repr__())

    def test_lastCard(self):
        deck = Deck()
        self.assertEqual('(K, HEARTS)', deck.stackOfCards[51].__repr__())

    def test_shuffle(self):
        deck = Deck()
        deck.shuffle()
        self.assertNotEqual('(A, SPADES)', deck.stackOfCards[0].__repr__())
        self.assertNotEqual('(K, HEARTS)', deck.stackOfCards[51].__repr__())

    def getRoy(self):
        roy = Player("roy") # local variable within function
        roy.addCardToHand(self.black_heartsA)
        roy.addCardToHand(self.black_clubsQ)
        return roy

    def getJohn(self):
        john = Player("John") # local variable within function
        john.addCardToHand(self.black_heartsA)
        john.addCardToHand(self.black_clubsQ)
        john.addCardToHand(self.black_diamonds4)
        return john

    def test_playerHand(self):
        roy = self.getRoy()
        card = roy.hand[0]
        self.assertEquals(card, self.black_heartsA)
        card = roy.hand[1]
        self.assertEquals(card, self.black_clubsQ)

    def test_cleanHand(self):
        self.roy.cleanHand()
        self.assertEquals(0, self.roy.getHandSize())

    def test_showHand(self):
        roy = self.getRoy()
        actual = roy.showHand()
        expected = "roy: [(A, HEARTS), (Q, CLUBS)]"
        self.assertEqual(expected, actual)

    def test_getHandValue(self):
        roy = self.getRoy()
        actual = roy.getHandValue()
        self.assertEqual(21, actual)

    def test_getHandValueWithAceBust(self):
        john = self.getJohn()
        actual = john.getHandValue()
        self.assertEqual(15, actual) # homework: how do I change code make this pass

    def testDealerHit(self):
        dealer = Dealer()
        dealer.addCardToHand(self.black_diamonds4)
        dealer.addCardToHand(self.black_diamonds4) # 8 in hand
        self.assertEqual(True, dealer.hit())
        dealer.addCardToHand(self.black_clubsQ) # 18 in hand
        self.assertEqual(False, dealer.hit())

