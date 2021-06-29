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
    '3': "Wednesday",
    '4': "Thursday",
    '5': "Friday",
    '6': "Saturday",
    '7': "Sunday",
}
print(days)

post = dict(message="SS contopoaxi",language="English")
print(d)

t = ((1,2),(3,4),(5,6)) 
d = dict(t)
print(d)

# get value from key in a dict
x = days['3']
print(x)

x = days.get('3')
print(x)

x = days.get('9','No such day!')
print(x)

if '9' in days: # before you get value from dict, you need check the existence of the key.
        x = days['9']
        print(x)
else:
        days['9'] = 'no such day.'

print(days)

# dict
print('done.')

