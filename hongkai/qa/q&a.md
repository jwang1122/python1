# My questions

[Useful Icons](../doc/myIcons.md)

✔️❌❓

* the split is including the punctuation
```py
str1 = 'I am so happy to learn Python which makes me happy, my parents happy, and also interested in Python Python Python Python Python.'
words = str1.split() #the split is including the punctuation
d = {}
for i in range(1,len(words)):
    str2 = words[i]
    if str2 in d:
        d[str2] += 1
    else:
        d[str2] = 1
print(d)
```