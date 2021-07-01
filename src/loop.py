# for loop on range() # iterable
for i in range(10):
    print(i, end=', ')
print()

# for loop on string
s = "hello world!"
for i in s: # loop for each character
    print(i, end=' ')
print()

# for loop on tuple
t=(1,3,5,7,9)
for s in t: # s is the variable for each element in the tuple, you can name it whatever
    print(s, end=' ')
print()

# for loop on list
cars = ["ford",'toyota','bmw','mazda']
for car in cars:
    print(car, end=", ")
print()

# for loop on set
set1 = {1,2,3,4}
for s in set1:
    print(s, end=', ')
print()

# for loop on dict
d = {1:'one', 2:'two', 3:'three'}
for num in d:
    print(num, '-', d[num], sep='', end=', ')
print()

# for loop break
for i in range(10):
    print(i, end=', ')
    if i > 3:
        break     # jump out from the loop
print()

# for loop continue
for i in range(10):
    if i < 2:
        continue  # skip the following code in the loop, continue to next step
    print(i, end=', ')
print()


# while loop
a, b = 0, 1 # initial value for loop variable a=0
while a<10:  # while loop condition, a is loop variable
    print(a+b, end=' ')
    a, b = a+1, a+b # adjust the condition variable
print()

# break on while loop
# count = 1
# while True: # infinite loop
#     answer = input(str(count) + ": Do you want to continue? (y/n) ")
#     if answer == 'n':
#         break
#     count = count + 1

# sum1 = 0
# while True:
#     x = int(input("Enter an integer: "))
#     sum1 += x
#     answer = input(str(count) + ": Do you want to continue? (y/n) ")
#     if answer == 'n':
#         print(f"sum = {sum1}")
#         break
#     count = count + 1

# continue on while loop
a = -1
while a<10:
    a += 1
    if a >2 and a < 7:
        continue # stop doing the following code, go back to the loop
    print(a)

print("Done.")

