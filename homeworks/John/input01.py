from math import pi
"""
Accept user input a float number,
output radius and circle area.

for example, 

Please enter radius of a circle: 1.1
r = 1.1
area = 3.8013271108436504

, where 1.1 is user input.
"""
userInput = input("Please enter radius of a circle: ")
radius = float(userInput) # must convet user input to a flot number for calculation below
circleArea = radius**2*pi 

print(f"r = {radius}")
print(f"circle Area = {circleArea}")
# keep only 3 decimal digits
# print(f"circle Area = {circleArea:.3f}")