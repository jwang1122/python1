"""
* Write a Python program to calculate sphere surface area with given radius. 

![](images/sphere-surface-area.jpg)

$$ SA = 4 \pi r^2 $$

For given radius = 3

Expected output:

The sphere surface area with radius=3 is 339.292.
"""
import math
r = float(input("Enter the radius: "))
sa = r**2 * math.pi * 4
print(f"The sphere surface area with radius={r} is {sa}.")