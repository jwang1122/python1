from math import pi

def circle_area(radius):
    return radius**radius*pi
    

if __name__ == '__main__':
    
    radius = 3
    a=circle_area(radius)

    print (f"The area with radius of {radius} is {a}")

