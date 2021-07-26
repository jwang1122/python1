"""
*  Write a function calculation() such that it can accept two variables and calculate the addition and subtraction of them. 
And also it must return both addition and subtraction in a single return call.

```py
def calculation(a, b):
    # Your Code

res = calculation(40, 10)
print(res)
```

Expected result:
(50, 30)
"""

def calculation(a, b):
    add = a + b
    sub = a - b
    return add, sub

if __name__ == '__main__':
    res = calculation(40, 10)
    print(res)