# loop on range()
for i in range(10):
    print(i, end=" ")
print()

# for loop on string 
s = "Hello world!"
for i in s:
    print(i, end = '')
print()

# for loop on tuple 
t = (1,3,5,7,9)
for num in t:
    print(num, end = ' ')
print()

# for loop on list 
cars = ['ford', 'toyota', 'bmw', 'mazda']
for car in cars:
    print(car, end = ', ')
print()

# for loop on set
set1 = {2, 4, 6, 8} # set is unordered
for e in set1:
    print(e, end = ", ")
print()

# for loop on dict
d = {1:'one', 2:'two', 3:'three'}
for key in d:
    print(key, d[key], sep = '-', end = ', ')
print()

# break on for loop
for i in range(10):
    print(i, end=" ")
    if i > 2:
        break # break loop under the condition
print()

# continue on for loop
for i in range(10):
    if i < 2 and i > 6:
        continue # continue the loop skip the following code block
    print(i, end = " ")
print()

# while loop: 1. initialize variable; 2. variable condition; 3. adjust the variable
a = 0
b = 1
while a < 10:
    a += 1
    print(a + b, end = ' ')
    b = a + b
print()

# continue on while loop
a = 0
while a < 10: # you can rewrite your for loop to while
    a += 1
    if a > 2 and a < 7:
        continue
    print(a)

# break on while loop
sum1 = 0
while True:
    x = float(input("Enter a number: "))
    sum1 += x
    answer = input("Do you want to conitnue? (y/n)")
    if answer== 'n':
        print(f"the total is {sum1}")
        break

print("Done")
