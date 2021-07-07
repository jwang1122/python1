"""
Define a function inside of a class
"""


class Robot:
    def hi(self): # class function has first positional argument as self
        print(f"Hi, I am {self.name}!") # robot introduce himself

    def add(self, x, y): # every inside function must have self argument
        return x + y

if __name__ == '__main__':
    x = Robot() # using default constructor to create an intance
    x.name = "John"
    x.hi() # when you call inside function, ignore self
    result = x.add(4,5)
    print(f"4 + 5 = {result}")
