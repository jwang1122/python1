"""
A function can return a function.

quadratic function:
f(x) = ax^2 + bx + c
"""

def quadratic(a, b, c):
    def f(x):
        return a*x**2 + b*x + c
    return f

if __name__ == '__main__':
    f = quadratic(2, 1, -3)
    print(type(f))
    x = 3
    print(f(x))

    f = quadratic(4, 5, 3)
    x = 3
    print(f(x))