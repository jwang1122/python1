"""
Logical Operator: often used with comparison opertor, 
    which has lower priority than comparison operator.

and: return True only both sides are True, return False otherwise  
or : return False only both sides are False, return True otherwise
not: return reverse result of comparison
"""

a, b = 10, 20

c = b==20 and a==b 
print(c)
c = b==20 or a==b 
print(c)
c = not a>b
print(c)

min1 = a<b and a or b
print(min1)

max1 = a>b and a or b
print(max1)

a = 0
c = a and b # c = a==0 and a or b; return b if a!=0, ortherwise return 0
print(c)

c = a or b # c = a==0 and b or a; return a if a!=0, return b otherwise
print(c)

c = a==0 and b or a
print(c)
