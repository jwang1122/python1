# Write a Python program to calculate sphere volume with given radius

from math import pi

r = float(input("For given radius = "))
a = 4/3 * pi * r**3

print(f"The sphere volume with radius={r} " + "is %.3f" %a)