# this doesn't really work

"""
* Find all possible unique subsets from a set of distinct integers.

for given set: [4, 5, 6]

Expected output:

```
[[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]
```

"""
class intSet:
    def __init__(self, thisSet):
        self.intSet = set(thisSet)
        self.intSubsets = set({})

    def __repr__(self):
        return str(self.intSet)
    
    def createSubsets(self):
        """
        doesn't really work
        """
        thisIntSet = list(self.intSet)[::-1]
        subsets = []
        subsets.append([])
        return subsets

if __name__ == '__main__':
    x = intSet({4, 5, 6})
    print(x.createSubsets())