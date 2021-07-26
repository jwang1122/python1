from math import pi

r = 1
area = pi * r**2

def circle_area(r):
    return (f"The area with radius={r} is " + "%.3f." %area)

a = circle_area(r)
print(a)