t=(1,2,3,4,5,6,3,4,5,)
print(type(t))
print(t)

# tuple is iterable
for item in t:
    print(item,end=', ')
print()

# tuple slicing
t1 = t[4:7]
print(t1)
t1 = t[:4]
print(t1)
t1 = t[4:]
print(t1)
t1 = t[1:7:2] # t[[start]:[end]:[step]
print(t1)
t1 = t[::-1]
print(t1)

# tuple is immutable (cannot be changed)
