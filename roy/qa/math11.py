temperature=input("Please enter temperature(45C/101F): ")
s = temperature[-1] # get last letter
if s=='F': # user input a Fahrenheit
    f = int(temperature[:-1]) # get all other string except the last letter
    c=5/9*(f-32)
    print(f"The temperature in Fahrenheit {f} is {c:.3f} in Celcius")
elif s=='C':
    c = int(temperature[:-1]) # get all other string except the last letter
    f=9/5*c+32
    print(f"The temperature in Celcius {c} is {f} in Farenheit")
