"""
* Write a recursive function to calculate the sum of numbers from 0 to 10

Expected Output:

55
"""

def sumOfNums0To10(stop = 10, numIn = 0):
    numOut = 0
    if numIn < stop:
        numOut = sumOfNums0To10(stop, numIn + 1)
    return numOut + numIn

if __name__ == '__main__':
    print(sumOfNums0To10())
