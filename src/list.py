"""
A List is an ordered collection of Python objects that is iterable,
mutable, separated by commas, surrounded by []. 方数组

l1 = [1,2,3,4]
"""

# Create a list
l1 = [] # empty list
l1 = [1,2,3,65,34,12,9,]
print(l1)
print(type(l1))
print(len(l1))

# compreshension vs. For
l1 = [i*i for i in range(10)]
print(l1)

l1 = list(range(0,16,5))
print(l1)

# nested list
faces = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
suits = ["Spade", "Club", "Diamond", "Heart"]
cards = [(face, suit) for face in faces for suit in suits]
print(cards)

# List is iterable
for item in l1:
    print(item, end=', ')
