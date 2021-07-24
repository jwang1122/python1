def outerFunc(a, b):
    def innerFunc():
        return a + b
    return innerFunc() + 5

if  __name__ == '__main__':
    a = 5
    b = 10
    x = outerFunc(a, b)
    print(x)