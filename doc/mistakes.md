# Mistakes in Python Class
## My mistakes

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

## Other's mistakes

## Syntax Errors

## Errors
### ❌cannot open image in markdown preview
✔️Solution: move **keyboard.md** under **doc/** folder.

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
