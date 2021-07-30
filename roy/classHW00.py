def f():
    pass

class A:
    pass

class Student:
    def __init__(self, name, id):
        self.name = name # createing instance level attribute
        self.id = id

    def turnInHomework(self):
        print(f"{self.name} turn in homework")


from math import pi

def circleArea(radius):
    return pi*radius**2

if __name__ == '__main__':
    s1 = Student("Angry Bonzo", "this is a id")
    s1.turnInHomework()
    x = circleArea(1)
    print(f"The circle area is {x}")
