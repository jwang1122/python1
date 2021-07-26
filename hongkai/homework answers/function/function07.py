"""
* Write program to Create a function that can accept two arguments name and age and print its value

```py
def printNameAge(name, age):
    # your code
```

printNameAge("John", 14)

Expected output:
John is 14 years old.
"""

def printNameAge(name, age):
    pluralAge = "s"
    if age == 1:
        pluralAge = ""
    printThis = f"{name} is {age} year{pluralAge} old."
    print(printThis)
if __name__ == '__main__':
    printNameAge("John", 14)