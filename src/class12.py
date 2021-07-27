"""
class level attribute vs. instance level attribute
"""
from circle import circleArea

class Dog:
    def __init__(self, name):
        self.tricks = [] # class level attribute self.tricks as empty list
        self.name = name # self.name is an instance level attribute

    def addTrick(self, trick):
        self.tricks.append(trick)

if __name__ == '__main__':
    x = circleArea(1)
    print(x)
    fido = Dog('Fido')
    fido.addTrick("roll over")
    print(f"Fido can do: {fido.tricks}")

    buddy = Dog('Buddy')
    buddy.addTrick("play dead")
    print(f"Buddy can do: {buddy.tricks}")

    print(f"Fido can do: {fido.tricks}")
