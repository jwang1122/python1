"""
class level attribute vs. instance level attribute
"""

class Dog:
    tricks = [] # class level attributes

    def __init__(self, name):
        self.name = name   # instance attribute

    def addTricks(self, trick):
        self.tricks.append(trick)

if __name__ == '__main__':
    fido = Dog("Fido")
    fido.addTricks("roll over")
    print(f"what fido can do: {fido.tricks}")

    buddy = Dog("Buddy")
    buddy.addTricks("Play dead")
    print(f"what buddy can do: {buddy.tricks}")

    print(f"what fido can do: {fido.tricks}")
