class Converter:
    def __init__(self, integer):
        self.number = integer

    def int2Roman(self):
        syb =     ("M", "CM", "D","CD", "C","XC","L","XL","X","IX","V","IV", "I")
        decimal = (1000, 900, 500, 400, 100, 90, 50,  40,  10,  9,  5,   4,    1)
        roman_num = ""
        i = 0
        while self.number >0:
            for j in range(self.number // decimal[i]): # floor divide
                roman_num += syb[i]
                self.number -= decimal[i]
            i+=1
        return roman_num

if __name__ == '__main__':
    c = Converter(101)
    x = c.int2Roman()
    print(x)