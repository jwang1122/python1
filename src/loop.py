# for loop on range(), range is iterable
from typing import Dict


for i in range(10):
    print(i, end=" ")
print()

#  for loop on string







t = (1,3,5,7,9)
for num in t:
    print(num, end=' ')
print()

# for loop on list
cars = ['ford','toyota', 'bmw', 'mazda']
for car in cars:
    print(car, end=', ')
print()

# for loop on set
set1 = {2, 4, 6, 8} # set is unordered
for e in set1:
    print(e, end=", ")
    print()

# for loop on dict
# for key in d:
#     print(key, d[key]), sep='-', end=', '
# print()

#break on for loop
for i in range(10):
    print(1, end=" ")
    if 1>2:
        break # break loop under the condition
print()

# continue on for loop
for i in range(10):
    if 1>2:
        continue# ocntinue the loop skip the following code block
    print(1, end=" ")
print()

# while loop: 1. initialize loop variable; 2. variable condition; 3. adjust the variable
a=0
b = 1
while a<10:
    a+=1
    print(a+b, end=' ')
    b = a + b
print()

# break on while loop
while True: # simulate do-while loop
    x = float(input("Enter a number: "))
    answer = input("Do you want to continue? (y/n)")
    if answer == 'n':
        break

print("Done")
