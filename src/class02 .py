"""
Define a function outside of the class
"""

def sayHello(obj): # someone else help robot to introduce itself
    print(f"Hello, I am {obj.name}!")

class Robot:
    pass

if __name__ == '__main__':
    x = Robot()
    x.name = "John"
    sayHello(x)

    