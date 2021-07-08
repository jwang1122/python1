"""
protected attribute: self._name
private attribute: self.__energy
"""

class Robot:
    def __init__(self, inputName=None, energy=1000):
        self._name = inputName # create a new attribute called self.name
        self.__energy = energy

    def __repr__(self):
        return self._name + ": " + str(self.__energy)

    def sayHello(self): # every function defined inside class has first positional argument as itself.
        if self.name:
            print(f"Hello, I am robot {self.name}.") 
        else:
            print('Hi, I am a robot without name yet.')

    def add (self, x, y): # self does NOT count as a argument
        return x + y


if __name__ == '__main__':
    robot1 = Robot(inputName="John") # use user defined constructor
    print(robot1)

    # print(robot1.__energy) # outside cannot access __energy in the Robot class.
    print(robot1._name) # same file can access the _name attribute
    print("Done")

    x = robot1.__energy # the __energy cannot be accessed outside
    print(x)
