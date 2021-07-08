"""
define constructor: __init__(self), object factory.
"""

class Robot:
    def __init__(self, inputName):
        self.name = inputName

    def sayHello(self): # every function defined inside class has first 
        print(f"Hello, I am robot {self.name}.")

    def add (self, x, y): # 
        return x + y
    

if __name__ == '__main__':
    robot1 = Robot("John") # use user defined constructor
    robot1.sayHello()
    print(robot1.name) # directly access the attribute name
    robot1.name = "Marvin" # change name
    robot1