"""
* Print multiplication table form 1 to 10

Expected output:

```output
  1   2   3   4   5   6   7   8   9  10 
  2   4   6   8  10  12  14  16  18  20 
  3   6   9  12  15  18  21  24  27  30 
  4   8  12  16  20  24  28  32  36  40 
  5  10  15  20  25  30  35  40  45  50 
  6  12  18  24  30  36  42  48  54  60
  7  14  21  28  35  42  49  56  63  70
  8  16  24  32  40  48  56  64  72  80
  9  18  27  36  45  54  63  72  81  90
 10  20  30  40  50  60  70  80  90 100
```
"""

# n = 0
# for i in range(10):
#     for j in range(10):
#         n = str((i+1)*(j+1))
#         space = 4-len(n)
#         print(n, end=space*" ")
#     print()

j = 0
for i in range(100):
    column = i%10
    col1 = False
    if column==0:
        j+=1
        print()
        col1 = True
    n = str((column+1)*j)
    space = 3-len(n)-col1
    print(space*" ",n, end='')