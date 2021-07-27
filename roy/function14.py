l = [8, 2, 3, -1, 7]
def mul(myList):
    result = 1
    for i in l:
        result *= i
    return result

if __name__ == '__main__':
    l = [8, 2, 3, -1, 7]
    
    print(mul(l))