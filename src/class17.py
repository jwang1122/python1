"""
Python module: enum
enumeration: the act of naming things seperatly, one by one:
"""

from enum import Enum

class Color(Enum): # Color class inherits from Enum class
    RED = 6 # where RED is the name, 6 is the value
    GREEN = 1
    BLUE = 3

if __name__ == '__main__':
    x = Color.GREEN
    print(x)
    print(x.name)
    print(x.value)
    print(type(x))
    print(type(x) is Color) # 'is' is an identity operator
    print(isinstance(x, Color))
    print(x == Color.RED)
    print(x == Color.GREEN)
    print(x is Color.GREEN)
    print(x in Color) # in is a membership operator

    # ENUM is iterable
    for c in Color:
        print(c, end = ' ')
    print()

    # Enum is callable
    animal = Enum('Animal',('ANT', 'DUDE', 'BEE', 'FOX')) # use tuple to build enumeration constants
    for a in animal:
        print(a, end = '  |  ')
    print()
    print(type(animal))

    animal = Enum('Animal',({'ants in me pants':1, 'DUDE':2, 'BEE':3, 'FOX':4}))
    for a in animal:
        print(a.name, end = '  |  ')
    print()

