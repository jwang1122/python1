"""
class level attribute vs. instance level attribute
"""

class Dog:
    tricks = [] # class level attributes

    def __init__(self, name):
        self.name = name # self.name is an instance level attibute

    def addTrick(self, trick):
        self.tricks.append(trick)

if __name__ == '__main__':
    fido = Dog("Fido")
    fido.addTrick("roll over")
    print(f"Fido can do: {fido.tricks}")

    buddy = Dog("Buddy")
    buddy.addTrick("Play dead")
    print(f"what buddy can do: {buddy.tricks}")

    print(f"what fido can do: {fido.tricks}")
