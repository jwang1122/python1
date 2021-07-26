
def removeValue(givenList, value):
    s = set()
    for i in givenList:
        s.add(i)
    s.remove(20)
    return list(s)

if __name__ == '__main__':
    
    givenList=[5, 20, 15, 20, 25, 50, 20]
    value = 20    
    
    set1 = set()
    

    

    print (removeValue(givenList, value))

