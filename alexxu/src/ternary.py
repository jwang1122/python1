"""
Ternary operator: if-else, and-or

if-else: a if a<b else b
1. first value
2. condition: if condition is True, return first value, 
3 another value, if condition is False, return another value.

and-or: a<b and a or b
1. condition
2. return first value if condition is True
3. return another value if condition is False
"""

a, b = 10, 20

# if-else ternary
min1 = a if a<b else b
print(min1) 

max1 = a if a>b else b
print(max1)

# and-or ternary
min1 = a<b and a or b
print(min1)

max1 = a>b and a or b
print(max1)

# use tuple and condition to choose value
max1 = (a, b)[a<b]
print(max1)
min1 = (a, b)[a> b]
print(min1)

min1 = min(a, b)
print(min1)
max1 



