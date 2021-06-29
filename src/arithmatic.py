# Math operators: +;-;*;/;%;**;// floor divisor
a, b = 10, 30
c1 = a + b
c2 = a - b
c3 = a * b
c4 = a / b
c5 = a % b
c6 = a**b
c7 = b//a

print(c1)
print(c2)
print(c3)
print(c4)
print(c5)
print(c6)
print(c7)

# why we need // operater?
a = 20
b = 3
c = a//b
print(type(c))
for i in range(c):
    print(i, end=' ')