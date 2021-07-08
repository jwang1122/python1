"""
define cconstructor with keyword argument
"""

class Robot:
    def __init__(self, inputName = None):
        self.name = inputName # create a new attribute called self.name

    def sayHello(self): # every method defined inside the class has first positional argument as itself
        if self.name:
            print(f"Hello, I am robot {self.name}.")
        else:
            print('Hi I am a robot without a name')
    
    def add (self, x, y): # self does NOT count as an argument
        return x + y


if __name__ == '__main__':
    robot1 = Robot("Kayden") # use user defined constructor
    robot1.sayHello()

    robot2 = Robot("Kayden") # you can use same class to create many instances
    robot2.sayHello()

    if(robot1 == robot2): # their the same?
        print("robot1 is same object as robot2")
    else:
        print("robot1 is not the same object as robot2")

    robot3 = robot1
    if(robot3 == robot1): # their the same?
        print("robot1 is same object as robot3")
    else:
        print("robot1 is not the same object as robot3")

     

