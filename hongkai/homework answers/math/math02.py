"""
* Write a Python program to calculate circle area with given radius.

![](images/circleArea.jpg)

$$ A = \pi r^2 $$

For given radius = 3

Expected output:

The circle area with radius=3 is 28.274333882308138.
"""
import math
r = float(input("Enter the radius: "))
a = r**2*math.pi
print(f"The circle area with radius={r} is {a}.")