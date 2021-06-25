"""
* Return the count of sub-string "Amy" appears in the given string.

For example:

```py
s = "Amy is good developer. Amy is a writer"
```

Expected output:

```output
'Amy' appeared 2 times in the give string.
```
"""

str1 = "Amy is good developer. Amy is a writer"
str2 = "Amy" # these first two strings can be changed! :)
length1 = len(str1)
length2 = len(str2)
count = 0
for i in range(0,length1-length2+1,1):
    str3 = ""
    for j in range(0,length2,1):
        str3 += str1[i+j-2]
    if str3 == str2:
        count += 1
print(f"'{str2}' appeared {count} times in the give string")
# if count is == 1, then it should say 1 time, not 1 times, but I'm too lazy