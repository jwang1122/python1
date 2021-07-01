"""
Multiply time operator: **
"""

# use ** as arthmathic op




# merge two dictionary 
x = {'key1':"value1","key2":'value2'}
y = {'key2':2, 'key3':3}







# get dict value 
date_info = {'year': "2020", 'month': "01", 'day': "01"}
track_info = {'artist': "Beethoven", 'title': 'Symphony No 5'}
filename = "{year}-{month}-{day}-{artist}-{title}.txt".format(**date_info, **track_info,)
print(filename)
