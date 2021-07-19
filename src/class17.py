"""
Python module: enum
enumeration: the act of naming things separately, one by one:
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
    print(x==Color.RED)
    print(x==Color.GREEN)
    print(x is Color.GREEN)
    print(x in Color) # in is a membership operator

    # Enum is iterable
    for c in Color:
        print(c, end=' ')
    print()

    # Enum is callable
    animal = Enum('Animal',('ANT','BEE','CAT','DOG')) # use tuple to build enumeration constants
    for a in animal:
        print(a.name, a.value, end=' | ')
    print()
    print(type(animal))

    animal = Enum('Animal', {'ANT':10,'BEE':21,'CAT':13,'DOG':54}) # use dict to build enumeration constants
    for a in animal:
        print(a.name, a.value, end=' | ')
    print()
    