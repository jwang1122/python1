from math import pi

"""
Function is a block of python code which can be called many times.
1. function name
2. argument list

def <functionName>(arguments):
    pass

function do nothing till you call it.
"""
def circleArea(radius):
    return pi*radius**2

radius = 1
area = circleArea(radius)
print(area)

# function return None if there is no return in the function
def sayHello(name):
    print(f"Hello, {name}!")
    
x = sayHello("John")
print(x)
