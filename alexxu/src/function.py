from math import pi

"""
Function is a bloke of python code which can be called many times.
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

# function may not return anything 
def sayHello(name):
  print("Hello, {name}!")
  return 5
 
x = sayHello("Gun Mage guy")
print(x)