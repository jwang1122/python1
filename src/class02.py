"""
Define a function outside of a class
"""

def hi(obj):
    print(f"Hi, I am {obj.name}!") # robot introduce himself

class Robot:
    pass

if __name__ == '__main__':
    x = Robot() # using default constructor to create an intance
    x.name = "John"
    hi(x)
