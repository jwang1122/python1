"""
* Write a Python program to calculate sphere volume with given radius. 

![](images/sphereVolume.png)

$$ V = \frac 4 3 \pi r^3 $$

For given radius = 3

Expected output:

The sphere volume with radius=3 is 113.097.
"""
import math
r = float(input("Enter the radius: "))
v = r**3 * math.pi * 4 / 3
print(f"The sphere volume with radius={r} is {v}.")