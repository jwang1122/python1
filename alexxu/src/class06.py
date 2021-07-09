"""
__repr__
__str__
__len__
"""

class A:
    def __repr__(self): # most of time, this function is enough for represent the object
        return "John"

   # def __str__(self): # print(a) use this function, and str(a) too
    #    return "Wang"

if __name__ == '__main__':
    a = A()
    print(a)
    print(repr(a))
    print(str(a))

