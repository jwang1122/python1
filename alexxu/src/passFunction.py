"""
pass a function to another function
"""
def mymath(a, b):
    return a+b, a-b, a*b, a/b


def add(a, b):
   return a + b

def mul(a,b):
    return a * b

def ff(f, x, y):
    return f(x,y)

if __name__ == '__main__':
    x = ff(add, 4, 5)
    print(x)
    add = 5 # override add function 
    x = ff(mymath, 4, 5)
    print(x)
    x = ff(mul, 4, 5)
    print(x)

 
