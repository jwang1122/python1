"""
define constructor with keyword argument" 
"""



class Robot:
     def __init__(self, inputName=None):
        self.name = inputName

def sayHallo(self):
    if self.Name:
        print(f"Hello, I am robot {self.name}.")
    else:
        print('Hi I am a robot without name yet.')

def add (self, s, y):
    return x + y 


if __name__ == '__main__':
    robot1 = Robot("John")
    robot1.sayHello()

    robot2 = Robot("Marvin")
    robot2.sayHello()

    if robot1 == robot2: # they are same?
        print("robot1 is same object as robot2")
    else:
        print("robot1 is not the same object as robot2")