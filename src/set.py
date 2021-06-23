""" 
A Set is an unordered collection Python objects that is iterable, 
mutable and separated by comma, has no duplicate elements, surrounded by {}.集合 

set1 = {1,2,3,4,5}
"""

# Create set
set1 = set()
set2 = set()

odds = set(range(1,11,2))
print(odds)

evens = set(range(0,11,2))
print(evens)

print(len(evens))

set3 = set([6,7,12,3,5,89])
print(set3)

# set is iterable
for el in evens:
    print(el, end=' ')
print()

# set licing
# x = odds[0]
# odds[1]=12

# modify set(add, discard, remove, pop)
set1 = set(range(1, 6))
set2 = set(range(3, 8))
print(set1)
print(set2)
set1.add(11)
print(set1)
set1.discard(3)
print(set1)
x=set1.pop()
print(x)
print(set1)
# set3 = set()
# set3.pop()
set1.remove(11)
print(set1)
# set1.remove(11)

# operator on set
# &: intersection
# |: union
# 
set1 = set(range(1, 6))
set2 = set(range(3, 8))
set3 = set1 & set2
print(set1)
print(set2)
print(f"intersection of set1 and set2 is {set3}")

# relationship between sets
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
set3 = set1.intersection(set2)
print(set3)

# set3 = set1 + set2
# print(set3)# 
set3 = set1 | set2
print(set3)
