"""
A set is an unordered collection of Python objects that is iterable,
mutable and has no duplicate elements, surrounded by {}.集合

set1 = {1,2,3,4}
"""

# Creating set
set1 = set()
set2 = set()

for i in range(1, 6):
    set1.add(i)

for i in range(3, 8):
    set2.add(i)

print(set1)
print(set2)

# set is iterable
for item in set1:
    print(item, end=', ')
print()
print(len(set1))
print(sum(set1))

# set slicing
# x = set1[3] # set is unordered, cannot be sliced

# modify set (add, clear, pop, remove)
set1.add(15)
print(set1)
set1.add(2) # no duplicate item allowed in set.
print(set1)

# Operator on set:
# & intersection
# | union
# > 
# <
# ==


# set management (union)

# Checking relation between sets