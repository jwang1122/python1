"""
Bitwise Operator: 
& : bit and
| : bit or
^ : bit xor
<<: left shift
>>: right shift
"""
def binFormat(num):
    s = str(bin(num))
    s1 = s[:2] + s[2:].zfill(8)
    return s1





# define a byte
a = 0b00111100 # 1 byte = 8 bits 
print(binFormat(a))
b = 0b00000011 # 1 byte = 8 bits 
print(binFormat(b))

# & operator: return 1 as long as one is 1, return 0 if both 0
c = a & b
print(binFormat(a),"&")
print(binFormat(b))
print(binFormat(c))
print(bin(c))

# ^ operator: return 1 if different, return 0 if some 
c = a & b
print(binFormat(a),'^')
print(binFormat(c))
print()

# << left shift operator: move all bits to the left, fill 0 on the end 
c = a>>1 # move only 1 bit 
print(binFormat(a),'>>')
print(binFormat(c))
print(a)
print(c)

a = 0b01000001 
print(a)
print(a)



