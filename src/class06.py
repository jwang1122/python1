"""
__repr__
__str__
__len__
"""

class A:
    def __repr__(self): # repr() function will use this function
        return "John"
    
    # def __str__(self): # print(a) and str(a) will use this function
    #     return "Wang"
    
    def __len__(self):
        return 5

if __name__ == '__main__':
    a = A()
    print(a)
    # print(repr(a))
    # print(str(a))
    li = [1,2,3,4,5,6,7]
    print(len(li))

    print(len(a)) # built in function len() will call __len__() in the class