"""
* Write a Python program to calculate surface area of a cylinder. 

![Cylinder Surface Area](images/cylinderSurfaceArea.png)

$$ A = 2 \pi r^2 + h(2\pi r) $$

Expected output:

```
Height of cylinder: 4
Radius of cylinder: 6

Volume is: 452.389
Surface Area is: 376.991
```
"""
import math
h = float(input("Enter the height: "))
r = float(input("Enter the radius: "))
sa = (r+h) * 2 * math.pi * r
v = math.pi * r**2 * h
str1 = "Height of cylinder: %.3f\nRadius of cylinder: %.3f\nVolume is: %.3f\nSurface Area is: %.3f"
print(str1 %(h,r,v,sa))