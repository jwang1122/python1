from math import pi

def circleArea(radius):
    if radius<0:
        raise ValueError(f"the radius must be positive number. You give {radius}")
    return pi*radius**2

if __name__ == '__main__':
    a = circleArea(2) # this block of code is your test area
    print(a)
    print("Done.")