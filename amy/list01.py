def findDivisible(numberList):
  for num in numberList:
    if (num % 5 == 0):
      print(num)

numList = [10, 20, 33, 46, 55]
print("Divisible of 5 in a list")
findDivisible(numList)