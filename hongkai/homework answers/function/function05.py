"""
* Define a function to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number.

Input: numbers= [10,20,30,40,50,60,70], target=60
Output: (1, 3)
"""

def findPair(list1, target): # wtfffffffffffffffffff
    for i in range(len(list1)):
        number1 = list1[i]
        list2 = list1
        for j in range(len(list2)):
            number2 = list2[j]
            if number1 + number2 == target:
                print(list1)
                return i, j

if __name__ == '__main__':
    numbers= [10,20,30,40,50,60,70]
    target=60
    pair = findPair(numbers, target)
    print(pair)
