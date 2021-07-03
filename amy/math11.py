# t = int(input("Please enter a temperature (45C, 101F): "))
# f = 9/5 * t + 32
# c = (5/9) * (f - 32)

# if t[-1] == 'C':
#     print(f"The temperature in Fahrenheit {f} is {c} in Celsius.")
# if t[-1] == 'F':
#     print(f"The temperature in Celsius {c} is {f} in Fahrenheit.")


temp = input("Please enter a temperature (45C, 101F): ")
degree = int(temp[:-1])
i_convention = temp[-1]

if i_convention.upper() == "C":
  result = int(round((9 * degree) / 5 + 32))
  o_convention = "Fahrenheit"
elif i_convention.upper() == "F":
  result = int(round((degree - 32) * 5 / 9))
  o_convention = "Celsius"
else:
  print("Input proper convention.")
  quit()
print("The temperature in", o_convention, "is", result, "degrees.")