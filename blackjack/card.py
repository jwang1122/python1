"""
Good thing: the face value is exactly the same showing on the card
Bad thing: People can use any string to generate a Card instance
"""
class Card:
    def __init__(self, face, suit):
        self.face = str(face)
        self.suit = suit
    
    def __repr__(self):
        return f"({self.face}, {self.suit})"

    def __eq__(self, other):
        return self.getValue() == other.getValue()
        
    def __gt__(self, other):
        return self.getValue() > other.getValue()

    def __lt__(self, other):
        return self.getValue() < other.getValue()

    def __add__(self, other):
        return self.getValue() + other.getValue()

    def getValue(self):
        pictured = {"A":1,"J":11,"Q":12,"K":13}
        if self.face.isdigit():
            return int(self.face)
        return pictured.get(self.face, 0)
        
if __name__ == '__main__':
    hearts2 = Card('2', 'Hearts')
    print(hearts2)

    diamonds2 = Card('2', 'Diamonds')
    print(hearts2==diamonds2)
    print(hearts2+diamonds2)

    clubsQ = Card('Q', 'Clubs')
    print(clubsQ+hearts2)