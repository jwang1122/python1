"""
# Define a function calculate volume of cylinder by given radius and height.

![](images/cylinderVolume.png)

```py
def cylinderVolume(radius, height):
    # your code here
```

Expected result:

The circle area with radius=1 and height=2 is ...
"""
from math import pi

def cylinderVolume(r, h):
    return pi * r**2 * h

if __name__ == '__main__':
    r = 1
    h = 2
    a = cylinderVolume(r, h)
    print(f"The circle area with radius={r} and height={h} is {a}.")