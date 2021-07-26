"""
* Write a python function to check whether a year (integer) entered by the user is a leap year or not.

Expected Output:

Input a year: 2017

The year 2017 is NOT a leap year.

Input a year: 2000

The year 2000 is a leap year.
"""

def determineLeapness(year):
    leapness = False
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                leapness = True
            #else False
        else:
            leapness = True
    #else False
    return leapness

def printLeapness(year):
    leapPrint = "NOT "
    if determineLeapness(year):
        leapPrint = ""
    printThis = f"The year {year} is {leapPrint}a leap year."
    print(printThis)

if __name__ == '__main__':
    printLeapness(2017)
    printLeapness(2000)

