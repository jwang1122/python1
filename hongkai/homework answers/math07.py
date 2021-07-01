"""
* Write a Python program to calculate volume of a cylinder. 

![Cylinder Surface Area](images/cylinderVolume.png)

$$ V = \pi r^2 h $$

Expected output:

```
Height of cylinder: 4
Radius of cylinder: 6

Volume is: 452.389
```
"""
import math
h = float(input("Enter the height: "))
r = float(input("Enter the radius: "))
v = math.pi * r**2 * h
str1 = "Height of cylinder: %.3f\nRadius of cylinder: %.3f\nVolume is: %.3f"
print(str1 %(h,r,v))