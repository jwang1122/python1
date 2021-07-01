"""
* Write a Python program to calculate area of a triangle with given base and height. 
![Rectangle Primeter](images/triangleArea.webp)
>$$ A = \frac 1 2 b \cdot h  $$
Expected output:

```output
Calculate area of a triangle:

base = 6
height = 4

area = 12 
```
"""
b = float(input("Enter the base: "))
h = float(input("Enter the height: "))
a = b*h/2
print("base = %.3f\nheight = %.3f\narea = %.3f" %(b,h,a))