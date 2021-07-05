from math import pi
h = 4
r = 6
v = round(pi*r*r*h, 3)
SA = round(2*pi*r*r + h*2*pi*r, 3)

print(f"Height of cylinder: {h}")
print(f"Radius of cylinder: {r}")

print(f"Volume is: {v}")
print(f"Surface Area is: {SA}")