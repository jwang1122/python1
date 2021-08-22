# this doesn't really work

"""
* Find all possible unique subsets from a set of distinct integers.

for given set: [4, 5, 6]

Expected output:

```
[[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]
```

"""
class FindSubSet:
    def __init__(self, thisSet):
        self.intList = list(thisSet)
        self.intSubsets = []

    def __repr__(self):
        return str(self.intList)
    
    def createSubsets(self):
        """
        doesn't really work
        """
        self.intSubsets.append([])
        self.intSubsets.append(self.intList)
        list1 = list(self.intList)
        for x in range(len(list1)):
            l2 = [self.intList[x]]
            self.intSubsets.append(l2)
            for y in range(x):
                l3 = [self.intList[x], self.intList[y]]
                self.intSubsets.append(l3)
        return self.intSubsets

    def subsetsRecur(self, current, sset):
        if sset:
            return self.subsetsRecur(current, sset[1:]) + self.subsetsRecur(current + [sset[0]], sset[1:])
        return [current]

if __name__ == '__main__':
    x = FindSubSet({4, 5, 6})
    print(x.createSubsets())

    mylist = x.subsetsRecur([], [4, 5, 6])
    print(mylist)