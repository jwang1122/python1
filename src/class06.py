"""
__repr__
__str__
__len__
"""

class A:
    def __repr__(self): # most of the time, this function is enough for represent the object
        return "Kayden"

    #def __str__(self): # print(a) use this function, and str(a) too
    #    return "Gao"

    def __len__(self):
        return 5

if __name__ == '__main__':
    a = A()
    print(a)
    print(repr(a))
    print(str(a))
    li = [1, 2, 3]
    print(len(li))
    print(len(a))
