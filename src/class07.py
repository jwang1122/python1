"""
define a protected attribute: self._name
define a private attribute: self.__energe
"""

class Robot:
    def __init__(self, inputName=None, energy=1000): # constructor
        self.__name = inputName
        self.__energy = energy # self._Robot__energy

    def __repr__(self):
        return self.__name + ": " + str(self.__energy)

    def hi(self): # class function has first positional argument as self
        if self.__name:
            print(f"Hi, I am {self.__name}!") # robot introduce himself
        else:
            print("Hi, I am a robot without name yet.")
            
    def add(self, x, y): # every inside function must have self argument
        return x + y

if __name__ == '__main__':
    robot1 = Robot("John") # call class constructor which is __init__()
    print(robot1) # name of the robot1 object can be accessed outside

    robot1._Robot__name = 'Marvin' # _Robot__name can be accessed outside
    robot1.hi()

    robot1.__energy = 2000 # __energy cannot be changed outside
    print(robot1)
