"""
Identity operator: is, is not
<<<<<<< HEAD
Always return True or False
=======
Always return True or False.
>>>>>>> 8f44d62b34f61f413ac87cfa479badc149f47826

"""

a = 5
b = 5
c = a

print(a is b)
print(a is c)

<<<<<<< HEAD
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
=======
c = 10 # peel off the label c put that label in the new location which store 10
print(a)
print(a is c) # a is no long c, this is only happens on premitive data type such as int, float.

l1 = [1,2,3,4,5]
l2 = l1
print(l1 is l2)

l2.append('hello') # if you change the content of l2, content of l1 will be changed as well
print(l1 is l2)
print(l1)

from turtle import turtle
>>>>>>> 8f44d62b34f61f413ac87cfa479badc149f47826
