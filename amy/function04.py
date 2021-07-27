from math import pi

def cylinderVolume(r, h):
    return pi*h*r**2


if __name__ == '__main__':
    r = 1
    h = 2
    cv = cylinderVolume(r, h)
    print(f"The circle area with radius={r} and height={h} is {cv:.3f}")