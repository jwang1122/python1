from math import pi

def circleArea(radius):
    if radius < 0:
        raise ValueError(f"Circle radius cannot be negative, but you enter {radius}.")
    return pi*radius**2

if __name__ == '__main__':
    radius = 2 # code block for developer to test their code defined in this file
    area = circleArea(radius)
    print(area)
    print("Done.")