"""
Function argument:
1. Function argument
2. keyword argument
"""
def f(a, b, /, c, d, *, e=5, f=6):
    """
    a, b are positional arguments only, because they are before /
    c, d are positional or keyword argument, because they are between /, and *
    e, f are keyword aregument only
    /, separator between positional only argument and keyword argument
    *, separator between positional argument annd keyword only argument 
    """
    print(a, b, c, d, e, f)


# call function without keyword argument because there is default value
f(1,2,3,4)
f(1,2,3,4,e='hello', f='world') # the default value will be override if you provide it
f(1,2,c=5,d=7)
f(1,2,d=5,c=7) # put c,d in diffrent order, you can change the keyword position 
# f(1,2,d=12,3) # always put positional first
f(1,2,f='f',d='d',c='c')