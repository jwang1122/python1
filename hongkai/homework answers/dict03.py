"""
* Create a new string variable with the value: 'I am so happy to learn Python which makes me happy, my parents happy, and also interested in Python Python Python Python Python.'

* Ceate a loop that goes through the string and finds how many times each word apperars, and save it to a dictionary.

📌**hints:** to split word in a string, try the following👇

```py
s = "Hello world"
words = s.split()
print(words)
```

Expected output:
{'I': 1, 'am': 1, 'so': 1, 'happy': 3, 'to': 1, 'learn': 1, 'Python': 6, 'which': 1, 'makes': 1, 'me': 1, 'my': 1, 'parents': 1, 'and': 1, 'also': 1, 'interested': 1, 'in': 1} 

"""

str1 = 'I am so happy to learn Python which makes me happy, my parents happy, and also interested in Python Python Python Python Python.'
words = str1.split() #the split is including the punctuation
d = {}
print(str1.count('Python'))
for i in range(1,len(words)):
    str2 = words[i]
    str2 = str2.strip(',.')
    if str2 in d:
        d[str2] += 1
    else:
        d[str2] = 1
print(d)
