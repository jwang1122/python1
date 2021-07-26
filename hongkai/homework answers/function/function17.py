"""
* Write a Python function to check whether a string is a valid password.

```
Password rules:
A password must have at least eight characters.
A password consists of only letters and digits.
A password must contain at least two digits.
```

Expected Output:

1. A password must have at least eight characters.
2. A password consists of only letters and digits. digits.
3. A password must contain at least two digits
Input a password (You are agreeing to the above Terms and Conditions.): abcd1234
Password is valid: abcd1234
"""

def checkTypeCount(password):
    allowed = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    for i in range(len(password)):
        if allowed.count(password[i]) == False:
            return False
    return True

def checkDigitCount(password):
    digitCount = 0
    for i in range(len(password)):
        if password[i].isdigit():
            digitCount += 1
        if digitCount >= 2:
            return True
    return False

def checkPassword(password):
    if len(password) >= 8:
        if checkTypeCount(password):
            if checkDigitCount(password):
                return True
    return False

def passwordFunc():
    print("1. A password must have at least eight characters.")
    print("2. A password consists of only letters and digits.")
    print("3. A password must contain at least two digits")
    password = input("Input a password (You are agreeing to the above Terms and Conditions.): ")
    validity = "in"
    returnBool = checkPassword(password)
    if returnBool:
        validity = ""
    printThis = f"Password is {validity}valid: {password}"
    print(printThis)
    return returnBool


if __name__ == '__main__':
    passwordFunc()