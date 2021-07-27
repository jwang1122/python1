"""
* Write a Python class named Rectangle constructed by a height and width 
and a function which will compute the area of a rectangle,
another function will compute the circumference (primeter).

Expected output:

```py
r1 = Rectangle(3, 4)
print(r1.area())
print(r1.circumference())
```
12

14
"""
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)


if __name__ == '__main__':
    r1 = Rectangle(3, 4)
    print(r1.area())
    print()
    print(r1.perimeter())