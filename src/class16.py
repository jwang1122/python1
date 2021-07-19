"""
class inheritance, review class level attribute
"""
class Superclass:
    def __init__(self, a):
        self.instancedata = a
    
    def __repr__(self):
<<<<<<< HEAD
        return str(self.instancedata) # str function converts tuple to a string, __repr__ can only retun str type
=======
        return str(self.instancedata) # str function converts tuple to a string, __repr__ can only return str type
>>>>>>> c5f0b46ebf07ba4ea36292d7f036c86e297d46d8

    def superFunc(self):
        print("superFunc() is running...")

class Subclass(Superclass): # Subclass inherits from Superclass
    def subFunc(self):
        print("subFunc() is running...")

if __name__ == '__main__':
    obj1 = Superclass("Super1")
    print(obj1)
    obj1.superFunc()

    obj2 = Superclass("Super2")
    print(obj2)

    obj3 = Subclass((1,2,3))
    print(obj3)
    obj3.superFunc()
    obj3.subFunc()

    # relationship of objects
    print(isinstance(obj3, Superclass))
    print(isinstance(obj3, Subclass))
    print(isinstance(obj2, Subclass))
<<<<<<< HEAD
=======
    
>>>>>>> c5f0b46ebf07ba4ea36292d7f036c86e297d46d8
