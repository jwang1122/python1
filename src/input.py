s = input("Enter a number: ")
print(type(s))
x = int(s)
print(type(x))
print(x+10)
print(s)

# s = input("enter a number: ")
# if s.isnumeric():
#     x = int(s)
#     print(x+4)
# else: 
#     print(s)

s = input("Enter temperature(45C/45F): ")
if s[-1]=='C':
    print("you inter a celcius temperature", s)
    # how about I want conver to Fahrenheit here
if s[-1]=='F':
    print("you inter a fahrenheit temperature", s)
    # how about I want conver to Celcius here

