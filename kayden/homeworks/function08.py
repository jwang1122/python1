#def func2 (x):
#    print(x)

#def func1(a, b, c, d, e, f):
#    return


def func1(x,y,z):
    print(x,y,z)

p = (4456,11,12)
func1(*p)


def func1(items):
    for a in items:
        print(a, end=' ')

func1([1,2,3,4])

