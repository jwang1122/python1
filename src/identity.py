# Identity Operator: is, is not; return True or False

a = 5
b = 5
c = a

print(a is b)
print(a is c)

a = str("john")
b = str("john")

print(a is b)

from turtle import Turtle
turtle1 = Turtle() # you create an instance of Turtle
turtle2 = Turtle()
print(turtle1 is turtle2)

l1 = list()
l2 = list()
l3 = l1
print(l1 is not l2) # return True because they are different memory location
print(l1 is l3)
l1.append(1)
print(l1)
print(l3)