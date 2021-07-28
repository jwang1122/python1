"""
* Write a Python class and define function to convert an integer to a roman numeral.

Expected result:
    1 ==> I
    4000 = MMMM

* define function to convert roman numeral to integer.

Expected result:
    DCLXXVI ==> 676
"""
class Converter:
    def __init__(self, integer):
        self.number = int(integer)
    
    def intToRoman(self):
        syb =     ("M" , "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I")
        decimal = (1000, 900 , 500, 400 , 100, 90  , 50 , 40  , 10 , 9   , 5  , 4   , 1)
        roman_num = ""
        i = 0
        while self.number > 0:
            for accessed in range(self.number // decimal[i]): # floor divided
                roman_num += syb[i]
                self.number -= decimal[i]
            i += 1
        return roman_num
    
if __name__ == '__main__':
    c = Converter(101)
    x = c.intToRoman()
    print(x)