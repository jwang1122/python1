"""
Multiple times operator: **
"""
a = 3
b = 2
c = a**b
print(c)

d1 = {'key1':'value1', 'key2':'value2'}
d2 = {'key2':2, 'key3':3}
d3 = {**d2, **d1} # merge two dictionary together, dict has no duplicated key
print(d3)

date_info = {'year': "2020", 'month': "01", 'day': "01"}
track_info = {'artist': "Beethoven", 'title': 'Symphony No 5'}
filename = "{year}-{month}-{day}-{artist}-{title}.txt".format(**date_info, **track_info,)
print(filename)
