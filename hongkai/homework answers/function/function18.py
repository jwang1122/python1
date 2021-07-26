"""
* Define a function that accepts 2 values and return its sum, difference, product, and quotient.

Expected output:

```
Enter a value a: 7
Enter a value b: 5

7 + 5 = 12
7 - 5 = 2
7 × 5 = 35
7 ÷ 5 = 1.4
```
"""


def operations():
    a = float(input("Enter a value a: "))
    b = float(input("Enter a value b: "))
    print()
    thisList = []
    thisList.append(f"{a} + {b} = {a + b}")
    thisList.append(f"{a} - {b} = {a - b}")
    thisList.append(f"{a} × {b} = {a * b}")
    thisList.append(f"{a} ÷ {b} = {a / b}")
    for task in thisList:
        print(task)

if __name__ == '__main__':
    operations()