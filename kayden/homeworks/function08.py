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


print()

def func1(*args):
    print(f"func1{args}")
    for i in args:
        print(i)

if __name__ == '__main__':
    func1(20, 40, 60)
    print()
    func1(80, 100, 'hello', 'kaydenthedude', (1,2,3), ["h", "j"])


