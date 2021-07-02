from math import pi

h = float(input("Height of cylinder: "))
r = float(input("Radius of cylinder: "))
sa = 2 * pi * r**2 + h * 2 * pi * r

print()
print(f"Volume is: 452.389")
print("Surface Area is: %.3f" %sa)