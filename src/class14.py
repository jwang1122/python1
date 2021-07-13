"""
internal function of a class calls another internal function
"""

class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)

if __name__ == '__main__':
    x = Bag()
    x.addtwice("apple")
    print(x.data)