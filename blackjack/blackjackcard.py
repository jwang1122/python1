from src.blackjack.card import Card # use this line for unit test
# from .card import Card # use relative path
# from card import Card # use this line for product

class BlackjackCard(Card):
    def getValue(self):
        switch = {"A":11,"J":10,"Q":10,"K":10}
        if self.face.isdigit():
            return int(self.face)
        return switch.get(self.face)

if __name__ == '__main__':
    heartsQ = BlackjackCard('Q', 'HEARTS') 
    print(heartsQ)
    print(heartsQ.getValue())