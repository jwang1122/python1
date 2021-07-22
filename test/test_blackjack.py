import unittest
from src.blackjack import *

class TestCard(unittest.TestCase):
    heartsA = Card("ACE", "HEARTS")
    diamonds4 = Card("4", "DIAMONDS")
    clubsQ = Card("QUEEN", "CLUBS")
    black_heartsA = BlackjackCard("ACE", "HEARTS")
    black_diamonds4 = BlackjackCard("4", "DIAMONDS")
    black_clubsQ = BlackjackCard("QUEEN", "CLUBS")

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
        self.assertEqual('(ACE, SPADES', deck.stackOfCards[0].__repr__())

    def test_lastCard(self):
        deck = Deck()
        self.assertEqual('(KING, HEARTS', deck.stackOfCards[51].__repr__())

    def test_shuffle(self):
        deck = Deck()
        deck.shuffle()
        self.assertNotEqual('(ACE, SPADES', deck.stackOfCards[0].__repr__())
        self.assertNotEqual('(KING, HEARTS', deck.stackOfCards[51].__repr__())


