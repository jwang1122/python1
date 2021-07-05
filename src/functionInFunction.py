"""
define inner functions inside outer function.
"""
def parent():
    print("I am parent...")
    def child1():
        print("I am elder child.")
    def child2():
        print("I am younger childer.")

    child1()
    child2()

if __name__ == '__main__':
    parent()
    # 1. OOP: encapsulation: avoid function called unexpected
    # 2. Functional Programming: return function from function
    # parent.child1() # AttributeError: 'function' object has no attribute 'child1'

