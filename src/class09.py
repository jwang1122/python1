"""
__new__(cls): object constructor, avoid override this function unless you have to
__init__(self): initializing the object
"""
class A:
    def __new__(cls): # ❓override default __new__()
        print("A.__new__() is called.") #✔️I want run this line before create the object
        return super(A, cls).__new__(cls)

    def add(self, x, y):
        return x + y

class B:
    def __init__(self): # use default __new__() to create instance
        print("B.__init__() iscalled.")

class C:
    def __init__(self, name): # initialize the object that __new__ created.
        print("C.__init__() iscalled.")
        self.name = name
        # return self.name # __init__ return nothing

    def __repr__(self):
        return self.name

    def __new__(cls): # constructor which create the object
        print("C.__new__() is called.") #
        return super(C, cls).__new__(cls) # return object
        # return 99 # return integer

if __name__ == '__main__':
    a = A() # try to create instance of A
    print(type(a))
    print(a.add(4,5))
    b = B()
    print(type(b))

    c = C()
    print(type(c))
    print(c)

