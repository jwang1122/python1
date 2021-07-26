def findMom(child):
    for childMom in nameList:
        if childMom[0] == x:
            return childMom[1]




if __name__ == '__main__':
    
    nameList = [
        ('james', 'mary'),
        ('john', 'patricia'),
        ('michael', 'jennifer'),
        ('david', 'linda'),
        ('susan', 'elizabeth'),
        ('nancy', 'barbara'),
    ]

    x = input("Please enter child name:")
    print(findMom(x))
