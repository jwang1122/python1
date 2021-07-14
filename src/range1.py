"""
in range function, there are 3 variables: start, stop, step
for range1 class, we want default value for start=1 not 0, include stop
"""

class range1:
    def __init__(self, *args): # where args is optional number of arguments
        self.start = 1 # default value of self.start = 1
        self.step = 1
        if len(args)==1:
            self.stop = args[0]
        if len(args)==2:
            self.start = args[0] # override default value by given value
            self.stop = args[1]
        if len(args)==3:
            self.start = args[0] # override default value by given value
            self.stop = args[1]
            self.step = args[2] # override default step to given value

    def __iter__(self): # make class range1 iterable
        self.current = self.start
        return self

    def __next__(self):
        if self.current > self.stop:
            raise StopIteration
        result = self.current
        self.current += 1
        return result
        
if __name__ == '__main__':
    r = range1(3, 10, 2)
    print(type(r))

    for i in range1(10): # one variable start
        print(i)
    print()

    for i in range1(5, 10): # two vaiables start, stop
        print(i)
    print()

    for i in range1(5, 10, 2): # three variables start, stop, step
        print(i)
