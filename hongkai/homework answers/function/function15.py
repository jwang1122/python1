"""
* define a function removeValue(givenList, value) that for given a Python list, remove all occurrence of value from the list

```py
list1 = [5, 20, 15, 20, 25, 50, 20]
removeValue(list1, 20)
```

Expected result:

[5, 15, 25, 50]
"""
def removeValue(givenList, value):
    for i in givenList:
        if i == value:
            givenList.remove(value)

if __name__ == '__main__':
    list1 = [5, 20, 15, 20, 25, 50, 20]
    removeValue(list1, 20)
    print(list1)