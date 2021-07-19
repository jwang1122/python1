"""

* define a function named findMom() by given name list of child and mom, and child name you are looking for, find who is his/her mom.

Sample name list:
```py
nameList = [
    ('james', 'mary'),
    ('john', 'patricia'),
    ('michael', 'jennifer'),
    ('david', 'linda'),
    ('sucan', 'elizabeth'),
    ('nancy', 'barbara'),
]
```
Sample input:

```input
Please enter child name: david
```

Expected output:

```output
david's mom is linda.
```
"""

nameList = [
    ('james', 'mary'),
    ('john', 'patricia'),
    ('michael', 'jennifer'),
    ('david', 'linda'),
    ('sucan', 'elizabeth'),
    ('nancy', 'barbara'),
]

def findMom(child):
    for i in nameList: # i is a tuple; nameList is a list
        if i[0] == child:
            return i[1]

if __name__ == '__main__':
    child = input("Please enter child name: ")
    mom = findMom(child)
    print(f"{child}'s mom is {mom}.")