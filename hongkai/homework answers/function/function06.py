"""
* test the following code, define a function named addList(l1, l2) to calculate addition for 2 list.

```py
l1 = [1,2,3]
l2 = [4,5,6]
l = l1+l2
print(l)
```

```java
def addList(l1, l2):
    pass
```

Expected result:

l = [5, 7, 9]

not
[1, 2, 3, 4, 5, 6]
"""

def addList(l1, l2):
    l = []
    for i in range(len(l1 if l1 < l2 else l2)):
        l.append(l1[i] + l2[i])
    return l

if __name__ == '__main__':
    l1 = [1,2,3]
    l2 = [4,5,6]
    l = addList(l1, l2)
    print(f"l = {l}")