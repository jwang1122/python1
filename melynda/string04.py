something = str(input("Enter a large four digit integer: "))
something = something[::-1]
thisThing = something[:1]
nothing = something[1:2]
anotherThing = something[2:3]
randomThing = something[3:4]
print(f"{thisThing} {nothing} {anotherThing} {randomThing}")