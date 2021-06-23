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
l1 = list("hello") # use list as function to create a list with iterable object
print(l1)

# compreshension vs. For
l1 = [i*i for i in range(10)]
print(l1)

l1 = list(range(0,16,5))
print(l1)

# nested list
faces = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
suits = ["Spade", "Club", "Diamond", "Heart"]
cards = [(face, suit) for face in faces for suit in suits]
# print(cards)

# List is iterable
for item in l1:
    print(item, end=', ')
print()
# for i in 10: # 10 is not iterable
#     print(i)

# list slicing
l1 = cards[3] # pick up sigle element in the list
print(l1)
l1 = cards[4:8] # [[start]:[stop]:[step]]
print(l1)
l1 = cards[::]
print(l1)
l1 = cards[::-1] # reverse the original list

# modify a list (append, insert, remove, pop)
l1 = [1,2,3,4,5]
l1[0] = 12 # modify single element in the list
print(l1)
l1.append(54) # add a new element at end of the list
print(l1)
l1.insert(2, 11) # insert single element
print(l1)
x=l1.remove(11) # remove function take value NOT index
print(l1)
print(x)
x = l1.pop(0) # default pop up last which is index=-1, stack
print(x)
print(l1)

# list can have mixed data type
student1 = ["Roy","Huang",11, "1234"]
student1=tuple(student1)
print("The student with name '%s %s' is %d years old, his/her id is %s." %student1)

# list can be nested
l1 = [[1,2],[2,3,4],["h"]]

# operator on list, +, *, 
l1 = [1,2,3]
l2 = [4,5,6]
list1 = l1 + l2
print(list1)
l1=[False,False,False,False]*4 # initialize value for big list
print(l1)

# use list and tuple together to find something
movies = [("Citizen Kane", 1941),("Spirited Away",2001),("It's a Wonderful Life",1946),("Gattaca",1997),("No Country for Old Men",2007),("Rear Window",1954),("The Lord of the Rings",2001),("Groundhog Day",1993),("Close Encounters of the Third Kind",1977),("The Royal Tenenbaums",2001),("The Aviator",2004),("Raiders of the Lost Ark",1981)]
before2000 = [(title, year) for (title, year) in movies if year<2000]
print(before2000)