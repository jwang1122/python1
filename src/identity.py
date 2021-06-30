"""
Identity operator: is, is not
Always return True or False

"""

a = 5
b = 5
c = a

print(a is b)
print(a is c)

c = 10 # peel off the lable c put that label in the new location which store 10
print(a)
print(a is c) # a is no longer c

l1 = [1,2,3,4,5]
l2 = l1 
print(l1 is l2)

l2.append('hello') # if change the conternt l2, content of l1 will be changed as well
print(l1 is l2)
print(l1)

from turtle import turtles