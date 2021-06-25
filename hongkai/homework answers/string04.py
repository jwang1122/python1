"""
* Write a code to extract each digit from an integer, in the reverse order

Sample input

```input
Enter an large integer: 7536
```

Expected output

```output
6 3 5 7
```
"""

n = input("Enter an large integer: ")
length = len(n)
# print(n)
for i in range(0,length,1):
    print(n[length-i-1], end=" ")