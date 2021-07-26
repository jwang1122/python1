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

    KaydentheDude = Player("KaydentheDude") # class level attribute
    KaydentheDude.addCardToHand(black_heartsA)
    KaydentheDude.addCardToHand(black_clubsQ)
    

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

    def getKaydentheDude(self):
        KaydentheDude = Player("KaydentheDude") # local variable within function
        KaydentheDude.addCardToHand(self.black_heartsA)
        KaydentheDude.addCardToHand(self.black_clubsQ)
        return KaydentheDude

    def getKaydentheDude(self):
        KaydentheDude = Player("KaydentheDude") # local variable within function
        KaydentheDude.addCardToHand(self.black_heartsA)
        KaydentheDude.addCardToHand(self.black_clubsQ)
        KaydentheDude.addCardToHand(self.black_diamonds4)
        return KaydentheDude

    def test_playerHand(self):
        KaydentheDude = self.getKaydentheDude()
        card = KaydentheDude.hand[0]
        self.assertEquals(card, self.black_heartsA)
        card = KaydentheDude.hand[1]
        self.assertEquals(card, self.black_clubsQ)

    def test_cleanHand(self):
        self.KaydentheDude.cleanHand()
        self.assertEquals(0, self.KaydentheDude.getHandSize())

    def test_showHand(self):
        KaydentheDude = self.getKaydentheDude()
        actual = KaydentheDude.showHand()
        expected = "KaydentheDude: [(A, HEARTS), (Q, CLUBS)]"
        self.assertEqual(expected, actual)

    def test_getHandValue(self):
        KaydentheDude = self.getKaydentheDude()
        actual = KaydentheDude.getHandValue()
        self.assertEqual(21, actual)

    def test_getHandValueWithAceBust(self):
        KaydentheDude = self.getKaydentheDude()
        actual = KaydentheDude.getHandValue()
        self.assertEqual(15, actual) # homework: how do I change code make this pass