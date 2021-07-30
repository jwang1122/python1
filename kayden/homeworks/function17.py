"""
Password rules:
1. A password mst have at least eight characters.
2. A password consists of only letters and digits.
3. A password must contain at least two digits.
"""

def isValidPassword(password):
    items = len(password)
    isValid = False # assume the password is NOT valid
    if items >= 8: # rule 1
        if password.isalnum():
            count = 0
            for s in password:
                if s.isdigit():
                    count+=1
            if count >=2:
                isValid = True
    if isValid:
        print(f"{x} is a valid password:")
    else:
        print(f"{x} is NOT a valid password")

if __name__ == '__main__':
    x = input("Enter a password: ")
    isValidPassword(x)