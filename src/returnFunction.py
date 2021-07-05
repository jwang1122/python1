"""
return a function from a function

f(x) = ax^2 + bx + c
"""

def quadratic(a, b, c):
    def qd(x):
        return a*x**2 + b*x +c
    return qd

if __name__ == '__main__':
    f = quadratic(3, 2, -4)
    print(f)
    print(f(5))
    f = quadratic(1, 3, 4)
    print(f)
    print(f(5))