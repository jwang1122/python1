"""
function defined outside of the class
"""

def f1(self, x, y): # define function one place, can be used for multiple class
    return min(x, x+y)

class A:
    f = f1 # we define class function by using outside function
    def g(self):
        return "hello world!"

class B:
    g = f1
    def add(self, x, y):
        return x + y
    
if __name__ == '__main__':
    # run the same function by different instance of different classes
    x = A()
    y = x.f(4,-3) # x is instance of A
    print(y)

    x = B()       # x is instance of B
    y = x.g(2, 4) 
    print(y)