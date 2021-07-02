"""
* Print downward Half-Pyramid Pattern with Star (asterisk)

Expected output

```output
* * * * *  
* * * *  
* * *  
* *  
*
```
"""
n = 5
for i in range(n):
    print("* "*(n-i))