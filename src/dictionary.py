"""
Dictionary is Python's implementation of a data structure 
that is more generally known as an associative array. 

A dictionary consists of a collection of key-value pairs. 
It is unordered, iterable, mutable, and each paire seperated by commas, 
surrounded by {}. The key-value pairs seperated by colon. no duplicate key in dict.

{'key1':1, 'key2':2}
"""

# create a dict (shortcut for dictionary)
d = {} # empty dictionary
print(type(d))
print(len(d))
d['key1'] = 'value1' # add one element into d
print(d)

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

post = dict(message="SS Contopaxi", language="English")
print(post)

t = ((1,2),(3,4),(5,6)) # how about list?
# t = (1,2,3,4,5,6) # even t is iterable, but python doesn't know how to convert to dict
d = dict(t)
print(d)

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

# dict is iterable
for i in days: # only return keys
    print(i)

for i in days: # return key and value 
    print(f"key:{i}, value:{days[i]}", end=" >>> ")
print()

# dict slicing
# x = d[1:4] # dict is unordered

# dict is mutable (modify existing, add new,)
# CRUD: Create, Retrieve, Update, Delete

post["userId"] = 'UID-1234' # Create: add new key-value pair
print(post)

x = post.get("userId")      # Retrieve
print(x)

print(days)
days['5']="Black Friday"     # Update change single key-value pair
print(days)

del post['userId']           # Delete key-value pair from the dictionary
print(post)

if 'address' in post:
    print(post['address'])

# nested dictionary
d1 = {'key1':'value1'}
d2 = {'key2':'value2'}
d1['key2'] = d2
print(d1) 

# operator on dict **
# d3 = d1 + d2
# d3 = d1 * 2
d1 = {1:'one', 2:'two'}
d2 = {2:'2', 3:'three'}
d3 = {**d1, **d2} # merge two dict to one dict without duplication
print(91, d3)


# dict function(items, keys, pop, values, clear)
x = days.items()
print(type(x))
for key, value in days.items():
    print(f"{key} is for {value}.")
print(93, key)
for key in days.keys():
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
