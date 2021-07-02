from math import fabs

"""
* print the following diamond pattern

```output
    *
   * *  
  * * *  
 * * * *  
* * * * *  
 * * * *  
  * * *  
   * *  
    *
```
"""
n = 5
for i in range(2*n-1):
    vShape = int(fabs(n-i-1))
    str = " " * vShape + "*" + " *" * (n - vShape - 1)
    print(str, sep="")
