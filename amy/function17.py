"""
Password rules:
must have at least eight characters
consists of only letters and digits
must have at least two digits
"""

def isValidPassword(password):
    items = len(password)
    isValid = False # assume the password is not valid
    if items >= 8: # rule 1
        if password.isalnum():
            count = 0
            for s in password:
                if s.isdigit():
                    count += 1
            if count > 2:
                isValid = True
    if isValid:
        print(f"{x} is a valid password")
    else:
        print(f"{x} is not a valid password")

if __name__ == '__main__':
    x = input("Input a password: ")
    isValidPassword(x)