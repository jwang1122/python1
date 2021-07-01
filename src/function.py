from math import pi

# define a function without calling, nothing happen
# function can be called many times
def circleArea(radius):
    return pi*radius**2

def sayHello(name): # function may return nothing
    print(f"Hello, {name}!")
    # return 5

# radius = 1
# area = circleArea(radius)
# print(area)

x = sayHello("John")
print(x)
