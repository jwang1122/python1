s = 'I am so happy to learn Python which makes me happy, my parents happy, and also interested in Python Python Python Python Python.'
list1 = s.split()
# print(list1)
d = {}
for word in list1:
    word = word.strip(',.')
    if word in d: 
        d[word] = d[word]+1
    else:
        d[word] = 1

print(d)
word = 'happy'
print(f"number of {word} in the string is {d[word]}")











#str1 = 'I am so happy to learn Python which makes me happy, my parents happy, and also interested in Python Python Python Python Python.'
#words = str1.split() 
#d = {}
#for i in range(words):
#    print(str1.count(words))
#print(words)