"""
compare:
__new__(cls) : constructor the object, return an instance
__init__(self): initializing the object, does NOT return anything
"""

class A:
    def __new__(cls): # ❓why we override __new__?
        print("A.__new__() is called.") # ✔️I want print this (do something before create the instance)
        # return 99 # __new__ can return object
        return super(A, cls).__new__(cls)
    def add(self, x, y):
        return x + y

class B:
    def __init__(self): # behind scene, __init__() also call default __new__()
        print("B.__init__() is called.")
        # return 99 # __init__ return None

class C:
    def __new__(cls): # if you define __new__, python will not call __init__
        print("C.__new__() is called.")
        return super(C, cls).__new__(cls)
    def __init__(self, name=None): # once you define __new__, the __init__ is useless
        print("C.__init__() is called.")

if __name__ == '__main__':
    a = A()
    print(type(a))
    print(a.add(4,5))
    b = B()
    print(type(b))
    c = C()
    print(type(c))