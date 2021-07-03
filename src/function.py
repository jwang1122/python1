from math import pi
"""
Function is a block python code which can be called many times.
1. function name
2. arguement list

def <functionName>(arguments):
    pass

function do nothing till you call it
"""
def circleArea(radius):
    return pi*radius**2

radius = 1
area = circleArea(radius)
print(area)

# function may not return None if there is no return in the function
def sayHello(name):
    print(f"Hello, {name}!")
    return 5

x = sayHello("Kayden")
print(x)