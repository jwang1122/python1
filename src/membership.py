"""
<<<<<<< HEAD
Membership Operator: in, not in

return True if the container contains the element, return False otherwise.

here are some containers: str, tuple, list, set, dict
"""
s = "Hello world!" # string container
=======
Membership operator: in, not in

Return True if the container contains the element, return False otherwise.

here is some container: str, tuple, list, set, dict
"""
s = "Hello, world!" # string container
>>>>>>> 8f44d62b34f61f413ac87cfa479badc149f47826
print('s' in s)

t = (1,2,3,4,5)
print(6 not in t)

l1 = [1,2,3,4,5]
print(3 in l1)

set1 = {1,2,3,4,5,"hello"}
print('hello' in set1)
<<<<<<< HEAD

t1 = ((1,2),(3,4),(5,6))
d = dict(t1)
print(2 in d) # in operator only care about key NOT value

=======

t1 = ((1,2),(3,4),(5,6))
d = dict(t1)
print(2 in d) # in operator only care about key NOT value
>>>>>>> 8f44d62b34f61f413ac87cfa479badc149f47826
