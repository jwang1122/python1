for i in range(10):
    print(i, end= " ")
    if i > 2:
        break #break loop under condition
print(10)

#continue loop
for i in range(10):
    if i > 2 and i<6:
        continue 
    print(i, end=" ")
print()

# while loop: 1. initialize loop variable 2. variable cond. 3. Adjust the variable
a=0
b=1
while a<10:
    a += 1
    print(a+b, end='')
    b = a+b
print(b)



