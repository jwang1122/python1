"""
* Given a range of the first 10 numbers, Iterate from the start number to the end number, and In each iteration print the sum of the current number and previous number

Expected output:

```output
Printing current and previous number sum in a range(10)
Current Number 0 Previous Number  0  Sum:  0
Current Number 1 Previous Number  0  Sum:  1
Current Number 2 Previous Number  1  Sum:  3
Current Number 3 Previous Number  2  Sum:  5
Current Number 4 Previous Number  3  Sum:  7
Current Number 5 Previous Number  4  Sum:  9
Current Number 6 Previous Number  5  Sum:  11
Current Number 7 Previous Number  6  Sum:  13
Current Number 8 Previous Number  7  Sum:  15
Current Number 9 Previous Number  8  Sum:  17
```
"""
for i in range(10):
    j = i-1
    ij = 2*i-1
    str = f"Current Number {i} Previous Number  {j}  Sum:  {ij}"
    if i == 0:
        str = "Current Number 0 Previous Number  0  Sum:  0"
    print(str)