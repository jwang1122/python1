"""
* Write a Python program to calculate primeter of a rectangle with given width and length. 

![Rectangle Primeter](images/rectangleArea.png)

>$$ A = length \cdot width  $$

Expected output:

```output
Calculate area of a rectagle:

length = 4
width = 6

area = 24 
```
"""
l = float(input("Enter the length: "))
w = float(input("Enter the width: "))
a = l*w
print(f"Calculate area of a rectagle:\n\nlength = {l}\nwidth = {w}\n\narea = {a}")