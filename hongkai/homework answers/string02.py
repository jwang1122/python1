"""
* Given a string and an integer number n, remove characters from a string starting from zero up to n and return a new string.

For example

```py
s = "pynative"
n = 4
```

Expected output

```output
The new string from n=4 to end is 'tive'. 
```
"""

str = "pynative"
n = 4
length = len(str)

print(f"The new string from n={n} to end is '", end="")
for i in range(n,length,):
    print(str[i], end="")
print("'.")

# I actually thought pynative was a real word