"""
class Inheritance
class level function
class level attribute (field, variable)
"""
from enum import Enum

class Mood(Enum): # Mood class inherits from Enum class, inherits from other's class is big advantage.
    FUNKY = 1 # class level constant attribute
    HAPPY = 3
    SAD = 5
    JEALOUS = 6

    def describe(self): # instance level function
        return self.name, self.value # return a tuple

    @classmethod # function decoration
    def favorite_mood(cls): # class level function
        return cls.HAPPY

    
if __name__ == '__main__':
    try:
        x = Mood.favorite_mood() # call class level function by using the class name, no need create instance
        print(x)
        print(Mood.FUNKY.value) # use class name to get class level attribute

        mood1 = Mood(1) # use value to get attribute
        print(type(mood1))
        print(mood1)
        print(mood1.favorite_mood()) # use the attribute to call class level function

        mood6 = Mood(6) # ValueError: 6 is not a valid Mood
        print(mood6)

        print(mood6.describe())
    except Exception as error:
        print(error)

    print("End")