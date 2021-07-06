from math import pi
def cylinderVolume(radius, height):
   return pi*radius*radius*height 

radius = 1
height = 2
v = round(cylinderVolume(radius, height), 3)

print(f"The circle area with radius = {radius} and height = {height} is {v}")

