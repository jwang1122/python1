"""
Membership Operator: in, not in
return True if the container contains the element, return False otherwise.

sample container: str, tuple, list, set, dict
"""

s = "Hello world!"
print('s' in s)

t = (1,2,3,4,5)
print('hello' not in t)

t = ((1,2),(3,4),(5,6))
d = dict(t)
print(d)
print(2 in d) # only check key not value
print(2 not in d)