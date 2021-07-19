def pair(inputList, target):
    x = len(inputList)
    for i in range(x):
        for j in range(i+1, x):
            y = inputList[i]+ inputList[j]
            if y==target:
                return i, j

if __name__ == '__main__':
    numbers= [10,20,10,40,50,60,70]
    target=60
    x = pair(numbers, target)
    print(x)
