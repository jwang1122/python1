"""
Function arguement:
1. positional arguement
2. keyword arguement
"""
def f(a, b, /, c, d, *, e = 5, f = 6):
    """
    a, b are positional arguements only, because they are before /
    c, d are positional or keyword arguement, because they are between /, and *
    e, f are keyword arguement only
    /, seperator between positional only argument and keyword argument
    *, seperator between positional argument and keyword only argument
    """
    print(a, b, c, d, e, f)


# call function without keyword arguement because there is default value
f(1, 2, 3, 4) # we treat c, d as positional argument
f(1, 2, 3, 4, e = 'hello', f = 'world') # the default value will be override if you provide it
f(1, 2, c = 5, d = 7)
f(1, 2, d = 5, c = 7) # put c, d in different order, you can change the keyword position
# f(1, 2, 3, d = 12, 3) # always put positional before keyword
f(1, 2, f = 'f', e = 'e', d = 'd', c = 'c')
f(1, 2, 3, 4, f = 2)
# f(a = 3, b = 4, c = 5, d = 6) # TypeError