"""
* Create an inner function to calculate the addition in the following way

1. Create an outer function that will accept two parameters, a and b
2. Create an inner function inside an outer function that will calculate the addition of a and b
3. At last, an outer function will add 5 into addition and return it

```py
result = outerFun(5, 10)
print(result)
```

Expected output:
20
"""

def outerFunc(a, b):
    def innerFunc():
        return a + b
    return innerFunc() + 5

if __name__ == '__main__':
    a = 5
    b = 10
    result = outerFunc(a, b)
    print(result)