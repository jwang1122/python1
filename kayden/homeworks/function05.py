number = [10, 20, 10, 40, 50, 60, 70]

for i in range(len(number)):
    for j in range(len(number)):
        print(i)
        print(j)
        if j != i: 
            
            print(number[i]+number[j])
        #and sum(number[i], number[j])== 60
         #   return "(i,j)"
