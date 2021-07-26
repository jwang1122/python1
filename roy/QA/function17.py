"""
Password rules:
A password must have at least eight characters.
A password consists of only letters and digits.
A password must contain at least two digits.
"""

x = input("Input a password (You are agreeing to the above Terms and Conditions.):")
items = len(x)
if items > 8 or items == 8:
    pass
elif items<8:
    print("password is not valid")
