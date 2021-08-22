"""
* Write a Python class to find the three elements that sum to zero from a set of n real numbers.

for given list:
 [-25, -10, -7, -3, 2, 4, 8, 10]

 Expected output:

 ```
Input list: [-25, -10, -7, -3, 2, 4, 8, 10]
Output: [[-10, 2, 8], [-7, -3, 10]]
 ```
"""

class ClassHW11:
    def threeSum(sefl, nums):
        result = []
        for x in range(len(nums)):
            for y in range(x+1, len(nums)):
                for z in range(y+1, len(nums)):
                    sum1 = nums[x] + nums[y] + nums[z]
                    if sum1 == 0:
                        result.append([nums[x], nums[y], nums[z]])
        return result

if __name__ == '__main__':
    x = ClassHW11() # using default constructor to create an instance
    nums = [-25, -10, -7, -3, 2, 4, 8, 10]
    print(x.threeSum(nums))