def findMom(nameList, childName):
    for pair in nameList:
        if pair[0]==childName:
             return pair[1]


child = input("Please enter child name: ")

nameList = [
    ('james', 'mary'),
    ('john', 'patricia'),
    ('michael', 'jennifer'),
    ('david', 'linda'),
    ('sucan', 'elizabeth'),
    ('nancy', 'barbara'),
]

mom = findMom(nameList, child)
print(f"{child}'s mom is {mom}")

