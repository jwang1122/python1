from math import pi

"""
A function is a block of organized, reusable code 
that is used to perform a single, related action.
* function name
* argument list
* function do nothing till you call it.

1. Python built-in functions
print()
len()
sum()
2. User defined function

def <functionName>(arguments):
    pass

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
