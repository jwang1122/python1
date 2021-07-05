temperature=input("Please enter temperature(45C/101F):")
s = temperature[-1]
if s=='F':
    f = int(temperature[:-1])
    c=5/9*(f-32)
    print(f"The temperature in Farenheit {f} is {c:.3f} in Celcius")
elif s=='C':
    c=int(temperature[:-1])
    f=9/5*c+32
    print(f"The temperature in Celcius {c} is {f} in Farenheit")
