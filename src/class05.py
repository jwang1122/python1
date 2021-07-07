"""
when print the object, print the name NOT memory address or object id.
"""

class Robot:
    def __init__(self, inputName=None): # constructor
        self.name = inputName

    def __repr__(self):
        return self.name

    def hi(self): # class function has first positional argument as self
        if self.name:
            print(f"Hi, I am {self.name}!") # robot introduce himself
        else:
            print("Hi, I am a robot without name yet.")
            
    def add(self, x, y): # every inside function must have self argument
        return x + y

if __name__ == '__main__':
    robot1 = Robot("John") # call class constructor which is __init__()
    robot1.hi()
    # x = robot1.hi # you have to use () when you call the function
    # print(type(x))
    print(robot1) # name of the robot1 object can be accessed outside

    robot1.name = 'Marvin' # robot1.name is changed outside
    robot1.hi()

    robot2 = Robot()
    robot2.hi()