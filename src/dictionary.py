"""
Dictionary is Python's implementation of a data structure 
that is more generally known as an associative array. 

A dictionary consists of a collection of key-value pairs. 
It is unordered, iterable, mutable, and each paire seperated by commas, 
surrounded by {}, and no duplicate key. The key-value pairs seperated by colon.

{'key1':1, 'key2':2}
"""
days = {
    '1': "Monday",
    '2': "Tuesday",
    '3': "Wendseday",
    '4': "Thursday",
    '5': "Friday",
    '6': "Saturday",
    '7': "Sunday",
}
print(days)

# Create a dictionary
d = {}
print(type(d))
print(len(d))

d1 = {
    '1': "Monday",
    '2': "Tuesday",
    '3': "Wendsday",
    '4': "Thursday",
    '5': "Friday",
    '6': "Saturday",
    '7': "Sunday",
}
print(d1)

post = dict(
    message="SS Cotopaxi", language="English"
)  # use dict() to create dict instance

t1 = ((1,2),(3,4),(5,6)) # dict(iterable)
d2 = dict(t1)
print(d2)

l1 = [(1,2),(3,4),(5,6)]
d2 = dict(l1)
print(d2)

# get value from key
x = days['4']
print(x)

x = days.get('5')
print(x)

# x = days['9']
# print(x)

if '9' in days:
    x = days['9']
    print(x)
else:
    days['9'] = 'no such days'

# dict is iterable
for i in days: # only iterate key
    print(i)  # print(i, d1[i])
print()

for i in days: # return key and value 
    print(f"key:{i}, value:{days[i]}", end=" >>> ")
print()

# check existence of a key before you get the value
if '5' in d1:
    print('5 is', d1['5'])


# dict slicing
# x = d1[1:4] # dict is unordered cannot be sliced 

# dict is mutable 
# CRUD: Create, Retrieve, Update, Delete
print(post)
post["userId"] = 1211      # Create a new key-value pair
print(post)
x = post['userId']         # Retrieve value by key
print(x)
post['userId'] = 'U1-1211' # Update value by given key
print(post)
del post['userId']         # Delete key-value pair from dictionary
print(post)

if "location" in post: # check if the key='location' in post dict
    print(post["location"])
else:
    print(f"no 'location' key")

# nested dictionary
d1 = {'key1':'value1'}
d2 = {'key2':'value2'}
d1['key3'] = d2
print(d1)

# operator on dict **
# d3 = d1 + d2
# d3 = d1 * 2
d1 = {1:'one', 2:'two'}
d2 = {2:'2', 3:'three'}
d3 = {**d1, **d2} # merge two dict to one dict without duplication
print(91, d3)

# dict function(items, keys, pop, values, clear)
x = d1.items()
print("106:",x)
print(type(x))

for key, value in d1.items():
    print(f"{key} is for {value}.")

x = d1.keys()
print("85:", x)
for key in d1.keys():
    print(key)

x = days.pop('3')
print(x)
print(days)

x = days.pop('9',"out of week range.")
print(x)

x = days.values()
print(x)

days.clear()
print(days)

