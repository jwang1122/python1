"""
A python class if for definig a particular type of object 
abstract from the real world.

Python class define data to represent the object state and
functions used to change the state of an object, or do something

1. class name (follow the naming convention)
2. attributes (data, state, variable)
3. functions (getter, setter, other functions)
"""

# define the most simplest class
class Robot:
    pass

if __name__ == '__main__':
    robot1 = Robot() # use the default constructor to create an istance of Robot class
    robot2 = Robot()

    print(robot1 == robot2)
    robot3 = robot1
    print(robot1 == robot3)
    # print(robot2.name) # AttributeError: 'Robot' object has no attribute 'name'

    robot2.name = "John"
    robot2.buildYear = 2000

    print(robot1.__dict__)
    print(robot2.__dict__)

    Robot.brand = 'Ge'
    print(Robot.__dict__)

    print(robot1.brand)
    print(robot2.brand)

    x = getattr(robot1, 'name')
    print(x)

    x = getattr(robot1, 'energy', 1000)
    print(x)