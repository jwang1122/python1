#number = [10, 20, 10, 40, 50, 60, 70]
#
#for i in range(len(number)):
#    for j in range(len(number)):
#        print(i)
#        print(j)
#        if j != i: 
#            
#            print(number[i]+number[j])
#        #and sum(number[i], number[j])== 60
#        #   return "(i,j)"

def pair(inputList, target):
    x = len(inputList)
    for i in range(x):
        for j in range(i+1, x):
            y = inputList[i] + inputList[j]
            if y==target:
                return i, j

if __name__ == '__main__':
    numbers= [10,20,10,40,50,60,70]
    target=60
    x = pair(numbers, target)
    print(x)