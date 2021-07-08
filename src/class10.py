"""
return instance for other class, another way to override __new__()
"""

class Sample(object):
    def __str__(self):
        return "SAMPLE"
    def add(self, x, y):
        return x + y

# use class A to create instance of class Sample
class A(object):
    def __new__(cls):
        return Sample()

class B(object):
    def __new__(cls):
        return super(B, cls).__new__(Sample)    

if __name__ == '__main__':
    a = A()
    print(type(a))
    print(a.add(4,5))
    print(a)

    b = B()
    print(type(b))
    print(b.add(6,11))
    print(b)

    print(a==b)