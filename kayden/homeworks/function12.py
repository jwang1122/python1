"""
recursive function is the functions call itself.
1. termination condition 
2. adjust the variable to meet the termination
"""

def sumOfNumber(number):
    if number == 0:# termination condition 
        return 0
    number -= 1
    return number + sumOfNumber(number)

if __name__ == '__main__':
    
    print(sumOfNumber(10))