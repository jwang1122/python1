"""
override __iter__, __next__ function
"""
class Reverse:
    """
    Iterator for looping over a sequence backwards
    """

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self): # this function makes this class iterable
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

if __name__ == '__main__':
    rev = Reverse("international")
    for c in rev:
        print(c, end='')
    print()

    rev = Reverse([1,2,3,4,5])
    for c in rev:
        print(c, end='')
    print()