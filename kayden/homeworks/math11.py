a = input("Please enter a temperature (45C, 101F): ")
if a=="45C":
    new=int(''.join(filter(str.isdigit, a)))
    print (new)
    x = (9/5)*new+32
    print(f"The temperature in Celsius {a} is {x}F in Fahrenheit")
if a=="101F":
    new=int(''.join(filter(str.isdigit, a)))
    print (new)
    x = round((5/9)*(new-32), 0)
    print(f"The temperature in Farehrit {a} is {x}C in Celsius")

