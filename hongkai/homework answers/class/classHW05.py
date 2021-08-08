"""
* Write a Python class named Circle constructed by a radius and a function which will compute the area of a circle, 
another function will compute the circumference (primeter).

Expected output:

```py
c1 = Circle(3)
print(c1.area())
print(c1.circumference())
```
12

14
"""
from math import pi

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return pi * self.radius**2

    def circumference(self):
        return 2 * pi * self.radius
    
if __name__ == '__main__':
    c1 = Circle(3)
    print(c1.area())
    print(c1.circumference())