"""
Python supports multiple inheritance
"""

class Base1:
    def __init__(self, name):
        self.name = name

    def add(self, x, y):
        return x + y

class Base2:
    def __init__(self, name, age=10):
        self.name = name
        self.age = age

    def mul(self, x, y):
        return x * y

    def __repr__(self):
        return self.name + ", age=" + str(self.age)

class Subclass(Base2, Base1): # multiple inheritance, the order is important, avoid function collision
    def sub(self, x, y):
        return x - y

if __name__ == '__main__':
    x = Base2("Base2",13)
    x = Subclass("Subclass") # AttributeError: 'Subclass' object has no attribute 'age'
    print(x)
    print(x.add(4,5)) # run function defined on Base1
    print(x.mul(4,5))
    print(x.sub(4,5))