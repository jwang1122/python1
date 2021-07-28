"""
# Python Homework

1. Find the answer for "what are the differences between class and function?".

Hints: python > help() > topics > CLASSES

You can also search online for the answer.

2. Define a student class based on the image below.

```mermaid
classDiagram

class Student{
    name:str
    id:int

    turnInHomework()
}
```

3. Define a function that calculate circle area.
![homework](../doc/images/20200529Homework.png)
4. write a test program to test your student class and area calculation function.
"""
from math import pi

def f():
    pass

class A:
    pass

class Student:
    def __init__(self, name, id):
        self.name = name # create instance level attributes
        self.id = id
    
    def turnInHomework(self):
        print(f"{self.name}, turn in your homework.")

def circleArea(radius):
    return pi * radius**2

if __name__ == '__main__':
    s1 = Student("Johnny", 1111)
    s1.turnInHomework()
    x = circleArea(2.3)
    print(f"the circle area is {x:.3f}")