"""
a Python class is for define a particular type of object abstracted from real world.

Python classes define what functions can be used to change the state of an object.

❓What is the state of an object?
✔️it is the attributes defined in the class.

1. class name (by naming convention, first letter should be Uppercase)
2. state (attribute variables)
3. function

define a Robot class
"""
# minimum definition of a class in Python
class Robot:
    pass

if __name__ == '__main__':
    robot1 = Robot() # use default constructor to create instance of a Robot
    robot2 = Robot()
    print(robot1==robot2)
    robot3 = robot1
    print(robot1==robot3) # different label on same memory location, so they are the same object

    robot1.name = "Marvin" # create an attribute for robot1 object
    robot1.buildYear = 2019

    print(robot1.name)
    print(robot1.buildYear)

    print(robot3.name)

    print(type(robot1) is Robot)

    Robot.brand = "GE" # use class name to add class level attribute
    print(robot1.brand) # every object of that class has same attribute
    print(robot2.brand)

    print(robot1.__dict__)
    print(robot2.__dict__)
    print(Robot.__dict__)

    x = getattr(robot1, 'name')
    print(x)

    x = getattr(robot2, 'energy', 1000)
    print(x)