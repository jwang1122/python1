"""
* Given a string, display only those characters which are present at an even index number.

For example: 

```py
s = "pynative"
```

Expected output:

```output
Orginal String is  pynative
Printing only even index chars:
p n t v
```
"""

str = "pynative"
length = len(str)
for i in range(0,length,2):
    print(str[i], end=" ")
#thx teacher