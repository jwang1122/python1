"""
A Tuple is an ordered collection of Python objects that is iterable, 
immutable, separated by commas surrounded by ()。圆数组

t1 = (1,2,3,4,5)
"""
# create a tuple
t = () # generate empty tuple
t = tuple()  # generate empty tuple
t = (9,)
t=(1,2,3,4,5,6,3,4,5,"hello")
print(type(t))
print(t)

# tuple is iterable
for item in t:
    print(item,end=', ')
print()

# tuple slicing
t1=t[3]
print(t1)
t1 = t[4:7]
print(t1)
t1 = t[:4]
print(t1)
t1 = t[4:]
print(t1)
t1 = t[1:7:2] # t[[start]:[end]:[step]
print(t1)
t1 = t[::-1]
print(t1)

# tuple is immutable (cannot be changed)
#t[3] = 10
#t.append(10)

# + add 2 tuples, * generate new tuple
t1 = (1,2,3)
t2 = (4,5,6)
t = t1 + t2
print(t)
t3 = ("firstname","lastname")
t = t3[:1] + t1 + t3[1:]
print(t)

t = t1*3
print(t)

# nested tuple
faces = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
suits = ("Spade", "Club", "Diamond", "Heart")
cards = tuple((face, suit) for face in faces for suit in suits)
print(len(cards))
print(type(cards))
print(cards)

# tuple can be used for an real object
student1 = ("Roy","Huang",11, "1234")
print("The student with name '%s %s' is %d years old, his/her id is %s." %student1)

book1 = ("Introduction Python", 10.99, 245)
print("the book with title of '%s' costs $%.2f has %d pages" %book1)

point = (3,5)

line = ((1,2),(9,11))

square = ((2,2),(2, 12),(12,12),(12,2))

# tuple is ordered by index group of items, so you can sort it
t = (3, 23,6,45,9,11,21)
t1 = tuple(sorted(t,reverse=True))
print(t)
print(t1)
# x=t.pop() # AttributeError
