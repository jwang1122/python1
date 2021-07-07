"""
assign name at object creation time.
"""

class Robot:
    def __init__(self, inputName): # constructor
        self.name = inputName

    def hi(self): # class function has first positional argument as self
        print(f"Hi, I am {self.name}!") # robot introduce himself

    def add(self, x, y): # every inside function must have self argument
        return x + y

if __name__ == '__main__':
    robot1 = Robot("John") # call class constructor which is __init__()
    robot1.hi()
    # x = robot1.hi
    # print(type(x))
    print(robot1) # name of the robot1 object can be accessed outside

    robot1.name = 'Marvin' # robot1.name is changed outside
    robot1.hi()
