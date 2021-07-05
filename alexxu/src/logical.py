"""
Logical Operator: 

and: return True only both sides are True, return False otherwise  
or : return False only both sides are False, return True otherwise
not: return reverse of comparison result
"""

a, b = 10, 20
c = a==10 and b==20
print(c)

c = a==20 or b==10
print(c)

c = not a==10
print(c)

min1 = a==b and a or b 
print(min1)
max1 = a>b and a or b
print("max number between a and b is",max1)

a=-130
c = a and b
print(c)

c = a or b 
print(c)





