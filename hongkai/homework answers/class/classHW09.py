"""
* Write a Python class named Converter, and define a function to convert an integer to a Roman numeral; and another function to convert Roman numeral to integer.

for example:

```py
print(Converter().int_to_Roman(1))
print(Converter().int_to_Roman(4000))
```

Expected output:

```
Roman Numeral for integer 1 is I.
Roman Numeral for integer 4000 is MMMM.
The integer for Roman Numeral MMMCMLXXXVI is 3986.
The integer for Roman Numeral MMMM is 4000.
```
"""

class Converter:
    def int_to_Roman(self, number):
        syb =     ("M" ,"CM","D","CD","C","XC","L","XL","X","IX","V","IV","I")
        decimal = (1000,900 ,500,400 ,100,90  ,50 , 40 ,10 ,  9 , 5 , 4  , 1)
        roman_num = ""
        i = 0
        while number > 0:
            for accessed in range(number // decimal[i]): # floor divided
                roman_num += syb[i]
                number -= decimal[i]
            i += 1
        str1 = f"Roman Numeral for integer {number} is {roman_num}."
        print(str1)
    
    def Roman_to_int(self, number):
        def findSybValue(symbol):
            sybTuple = ("M" ,"D","C","L","X","V","I")
            decimal =  (1000,500,100, 50, 10, 5 , 1 )
            for i in range(12):
                if sybTuple[i] == symbol[0]:
                    return decimal[i]
            return decimal[i]
        
        item = 0
        roman_num = number[::-1]
        total = 0
        prevItem = 0
        for i in range(len(roman_num)):
            item = findSybValue(roman_num[i])
            if item < prevItem:
                total -= item
            else:
                total += item
            prevItem = item
        str1 = f"The integer for Roman Numeral {number} is {total}."
        print(str1)

if __name__ == '__main__':
    Converter().int_to_Roman(1)
    Converter().int_to_Roman(4000)
    Converter().int_to_Roman(6942)
    Converter().Roman_to_int("MMMCMLXXXVI")
    Converter().Roman_to_int("MMMMMMCMXLII")
    Converter().Roman_to_int("MMMM")
    Converter().Roman_to_int("I")


