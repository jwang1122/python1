"""
* Write a Python function to multiply all the numbers in a list.

l = [8, 2, 3, -1, 7]

Expected result:

-336
"""

def productOfList(nums, numIn = 0):
    numOut = 1
    if numIn < len(nums)-1:
        numOut = productOfList(nums, numIn + 1)
    return numOut * nums[numIn]

if __name__ == '__main__':
    l = [8, 2, 3, -1, 7]
    print(productOfList(l))