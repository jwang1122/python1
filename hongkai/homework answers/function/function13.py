"""
* Write a Python function to find the Max of three numbers.

for example:

```py
max = maxOfThree(12, 4, 24)
print(max)
```

Expected output:
24
"""

def maxOfThree(a, b, c):
    ab = a if a > b else b
    abc = ab if ab > c else c
    return abc

if __name__ == '__main__':
    max = maxOfThree(12, 4, 24)
    print(max)