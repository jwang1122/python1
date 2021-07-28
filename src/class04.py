"""
define constructor: __init__(self), object factory.
"""

class Robot:
    def __init__(self, inputName):
        self.name = inputName # create a new attribute called self.name

    def __repr__(self): # this dunder function returns a represent string for this object
        return self.name

    def sayHello(self): # every function defined inside class has first positional argument as itself.
        print(f"Hello, I am robot {self.name}.") 
    
    def add (self, x, y): # self does NOT count as a argument
        return x + y


if __name__ == '__main__':
    robot1 = Robot("KaydentheDude") # use user defined constructor
    robot1.sayHello()
    print(robot1.name) # directly access the attribute name 
    robot1.name = "EthantheBoi" # change name directly outside which unsafe
    robot1.sayHello()
    print(robot1)
    
    
    