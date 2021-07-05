"""
Pass a function to another function
"""
def mymath(a, b):
    return a+b, a-b, a*b, a/b

def add (a, b):
    return a + b

def mul(a, b):
    return a * b

def ff(f, x, y): # Part of Functional Programming, the goal of ff is calculation
    return f(x, y)

if __name__ == '__main__':
    x = add(4,5)
    print(x)
    # add = 5 # override add function
    x = ff(add, 4, 5)
    print(x)
    x = ff(mul, 4, 5)
    print(x)
    x = ff(mymath, 4, 5)
    print(x)
