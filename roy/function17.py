"""
Password rules:
1. A password must have at least eight characters.
2. A password consists of only letters and digits.
3. A password must contain at least two digits.
"""



def isValidPassword(password):
    items = len(x)
    isValid = False
    if items >= 8: # rule 1
        if x.isalnum():
            count = 0
            for s in x:
                if s.isdigit():
                    count+=1
            if count >= 2:
                isValid = True
                print(f"{x} is a valid password")
            else:
                isValid = False
    if isValid:
        print(f"{x} is a valid password")
    else:
        print(f"{x} is NOT a valid password")


if __name__ == '__main__':
    x = input("Input a password:")
    isValidPassword(x)