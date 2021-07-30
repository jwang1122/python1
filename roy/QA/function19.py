def findMom(child):
    for childMom in nameList:
        if childMom[0] == child:
            return childMom[1]
    return "NOT in our list"

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
    print(f"{x}'s mom is {findMom(x)}.")


