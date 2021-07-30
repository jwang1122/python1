from math import pi

def cylinderVolume(radius, height):
    return radius**2*pi*height


if __name__ == '__main__':
    radius = 1
    height = 2
    cV=cylinderVolume(radius, height)
    print (f"The cylinder volume with radius = {radius} and height = {height} is {cV:.3f}")
