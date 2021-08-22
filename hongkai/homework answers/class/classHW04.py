"""
* Write a Python program to get the class name of an instance in 
Python, and the namespace of the said class.

For example, for Circle class, replace the ellipse ... with 
an expression.

```py
c = Circle()
print(...)
```

the output should be:
```
The class name of the instance c is 'Circle'.
__module__
area
diameter
__dict__
__weakref__
__doc__
<function Circle.area at 0x000002072FA45670>
```
"""
class Circle:
    def __init__(self):
        pass

    def area():
        pass 

if __name__ == '__main__':
    c = Circle()
    print(type(c).__name__)
    print(Circle.__dict__)