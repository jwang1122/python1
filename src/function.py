from math import pi
"""
A function is a block of organized, reusable code 
that is used to perform a single, related action.

1. Python built-in functions
print()
len()
sum()
2. User defined function
circleArea()
"""

# define a function without calling, nothing happen
# function can be called many times
def circleArea(radius):
    return pi*radius**2

def sayHello(name): # function may return nothing
    print(f"Hello, {name}!")
    # return 5

def mymath(x, y): # bad example, violate single response
    return x+y, x-y, x*y, x/y
 
# circleArea = 3.14 # override the function that make the function no longer works
radius = 1
area = circleArea(radius)
print(area)

x = sayHello("John")
print(x)

x = mymath(4,5)
print(type(x))
print(x)
