from math import pi

def circleArea(radius):
    if type(radius) not in [float, int]:
        raise TypeError(f"The radius of a circle must be a 'float' or a 'int' data type.")
    if radius < 0:
        raise ValueError(f"Circle radius cannot be negative, but you enter {radius}.")
    return pi*radius**2

def circumference(radius):
    return 2 * pi * radius

if __name__ == '__main__':
    radius = 3 # code block for developer to test their code defined in this file
    area = circleArea(radius)
    print(area)
    print(circumference(radius))
    print("Done.")