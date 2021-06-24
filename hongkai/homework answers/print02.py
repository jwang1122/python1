# variable assigner
from math import pi
r = input("Enter the radius: ")
r = float(r)
# this is where the math is
A = 4/3 * pi * r **3
# printer
print("The volume of a sphere with radius %f is %f" %(r,A))