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
        print(f"{self.name} turn in the homework please.")


def circleArea(radius):
    return pi * radius**2

if __name__ == '__main__':
    s1 = Student("boi", 6969)
    s1.turnInHomework()
    x = circleArea(2.3)
    print(f"the circle area is {x:.3f}")