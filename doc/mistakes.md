# Mistakes in Python Class
## My mistakes

❌The Unit test cannot be run!
✔️You can only run unit test by clicking **Testing** icon on left tool bar.

* ❌TypeError due to input string
```output
Traceback (most recent call last):
  File "c:\Users\12818\workspace\python1\src\print.py", line 5, in <module>
    print("%s is %d years old." %(name,age))
TypeError: %d format: a number is required, not str
```
👎The promblem code below
```py
name = input("Enter your name: ")
age = input("Enter your age: ")
print("%s is %d years old." %(name,age))
```
✔️The solution below, change %d to %s
```py
print("%s is %s years old." %(name,age))
```
✔️The solution below convert string input to integer
```py
name = input("Enter your name: ")
age = int(input("Enter your age: "))
# %d is a second placeholder which holds an integer
# %s is a first placeholder which holds a string
print("%s is %d years old." %(name,age))
print("after 5 years you will be %d years old." %(age+5))
```

❌The Unit test connot be run!
✔️You can only run unit test by clicking **Testing** icon on left-hand tool bar

## Other's mistakes

## Syntax Errors

## Errors
### ❌cannot open image in markdown preview
* ✔️Solution: move **keyboard.md** under **doc/** folder.

### ❓Why my cls command does NOT work?


### ❌Python sytax error
```output
  File "c:\Users\12818\workspace\python1\hello.py", line 1
    print("the area of rectangle is "%d, %area)
                                         ^     
SyntaxError: invalid syntax
```
* ✔️💡should put %d inside the double quote.
```py
area=3.14
print("the area of rectangle is %f." %area)
```

❌ override both __new__ and __init__
```py
class C():
    def __new__(cls): 
        print("C.__new__() is called.", name)
        cls.name = name
        return super(C, cls).__new__(cls)

    def __repr__(self):
        return self.name

    def __init__(self, inputName):
        print("C.__init() is called")
        self.name = inputName

if __name__ == '__main__':
    a = A()
    print(type(a))
    print(a)

    c = C("John")
    print(type(c))
    print(c)
```

```output
  File "c:\Users\12818\workspace\Terry\python1\src\class\class09.py", line 30, in <module>        
    c = C("John")
TypeError: __new__() takes 1 positional argument but 2 were given
```
✔️Obviously, if you override both __new__ and __init__ function, python will use __new__ create instance, which cause problem. conclusion: don't override __new__().