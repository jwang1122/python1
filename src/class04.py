"""
define cconstructor: __init__(self) object factory.
"""

class Robot:
    def __init__(self, inputName):
        self.name = inputName # create a new attribute called self.name

    def sayHello(self): # every method defined inside the class has first positional argument as itself
        print(f"Hello, I am robot {self.name}.")
    
    def add (self, x, y): # self does NOT count as an argument
        return x + y

if __name__ == '__main__':
    robot1 = Robot("Kayden") # use user defined constructor
    robot1.sayHello()
    print(robot1.name)# directly access the attribute name
    robot1.name = 'Dude' # change name
    robot1.sayHello()
    