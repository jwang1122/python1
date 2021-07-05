from math import pi

def circleArea(radius):
    if type(radius) not in [int, float]:
        raise TypeError(f"circle radius can only be int or float, but you enter '{radius}'")
    if radius < 0:
        raise ValueError(f"Circle radius cannot be negative, but you enter '{radius}'.")
    return pi*radius**2

if __name__ == '__main__':
    try:
        radius = 2.3# code block for developer to test their code defined in this file
        area = circleArea(radius)
        print(area)
        radius = 1.2# code block for developer to test their code defined in this file
        area = circleArea(radius)
        print(area)
    except Exception as error:
        print(error)
    print("Done.")