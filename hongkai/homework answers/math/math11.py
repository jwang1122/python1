#???
"""
* Write Python progrom recieve user input of temperature, convert from Celsius to Fahrenheit or vice versa. for instance, if user input 101F, which represents a Fahrenheit temperature, your output should be 38C.

here is the formula

$$ °F = \frac 9 5 °C + 32 $$
$$ °C = \frac 5 9 (°F - 32) $$

Expected output

```output
Please enter a temperature (45C, 101F): 101F
The temperature in Fahrenheit 101°F is 38°C in Celsius.

Please enter a temperature (45C, 101F): 45C
The temperature in Celsius 45C is 113F in Fahrenheit.
```
"""

def tempToFloat(temp):
    tempEnd = temp[len(temp)-1]
    allowedEnds = ("F", "f", "C", "c")
    if tempEnd == "F" or tempEnd == "f":
        returnTempEnd = "F"
    returnTemp = float(temp[0:len(temp)-1])
    if returnTemp.is_integer:
        return temp, returnTempEnd
    return "Not valid format"

def tempConvert(tempInput):
    temp = tempToFloat(tempInput)
    if type(temp) != float:

    letterEnd = temp[len(temp)-1]
    if letterEnd == "F" or letterEnd == "f":
        temp2 = (temp1-32)*5/9
        str1 = "The temperature in Fahrenheit %.3f°F is %.3f°C in Celsius." %(temp1,temp2)
    elif letterEnd == "C" or letterEnd == "c":
        temp2 = temp1*9/5+32
        str1 = "The temperature in Celsius %.3f°C is %.3f°F in Fahrenheit." %(temp1,temp2)
    else:
        str1="No such temperature unit."
    print(str1)


tempInput = input("Please enter a temperature: ")
tempConvert(tempInput)
# if tempInput.count("F") == 1:
#     tempConvert(tempInput)
# if tempInput.count("f") == 1:
#     tempConvert(tempInput)
# if tempInput.count("C") == 1:
#     tempConvert(tempInput)
# if tempInput.count("c") == 1:
#     tempConvert(tempInput)
print("Done.")
