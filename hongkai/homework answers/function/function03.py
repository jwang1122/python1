from math import pi

"""
# Define a function calculate area of circle by given radius

```py
def circle_area(radius):
    # your code here

r = 1
a = circle_area(r)
print(a)
```
Expected result:

The circle area with radius=1 is 3.142
"""
def circle_area(radius):
    return pi * r**2

if __name__ == '__main__':
    r = 1
    a = circle_area(r)
    print("The circle area with radius=%d is %.3f" %(r, a))

# The circle area with radius=1 is 3.142