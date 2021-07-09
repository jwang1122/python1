"""
a trick about override __new__()
make one class create another class instance possible
"""

class Sample(object):
    def __str__(self):
        return "SAMPLE"
    def add(self, x, y):
        return x + y

class A(object):
    def __new__(cls): # override __new__() then it never create instance of A
        return Sample() # return instance of another class
    def mul(self, x, y):
        return x * y

class B(object):
    def __new__(cls):
        return super(B, cls).__new__(Sample) # this will return an instance of Sample

if __name__ == '__main__':
    a = A() # try to create instance A
    print(type(a))
    print(a.add(4,5))

    b = B()
    print(type(b))