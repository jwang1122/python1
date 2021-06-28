s = "pynative"
# string is iterable

length = len(s)

print(f"Orginal String is {s}")
print("Printing only even index chars:")
for i in range(length):
    if i%2 ==0:
        print(s[i], end=' ')