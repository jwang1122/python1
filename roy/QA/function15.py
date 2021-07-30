def removeValue(givenList, value):
    s = set()
    for i in givenList:
        s.add(i) # remove duplicated value
    s.remove(value)
    return sorted(list(s))

if __name__ == '__main__':
    
    givenList=[5, 20, 15, 20, 25, 50, 20]
    value = 20

    print (removeValue(givenList, value))
