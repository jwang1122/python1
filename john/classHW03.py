class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length

    def circumference(self):
        return 2*(self.width + self.length)

if __name__ == '__main__':
    r1 = Rectangle(3, 4)
    print(r1.area())
    print()
    print(r1.circumference())
