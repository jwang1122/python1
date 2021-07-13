"""
class inheritence, review class level attribute
"""
class Superclass:
    def __init__(self, a):
        self.instancedata = a
        
    def __repr__(self):
        return self.instancedata

    def superFunc(self):
        print("subFunc() is running...")

class Subclass(Superclass): # Subclass inherits from Superclass
    def subFunc(self):
        print("subFunc() is running...")

if __name__ == '__main__':
    obj1 = Superclass("Super1")
    print(obj1)
    obj1.superFunc()

    obj2 = Superclass("Super2")
    print(obj2)

    obj3 = Subclass((1, 2, 3))
    print(obj3)
    obj3.superFunc()
    obj3.subFunc()
