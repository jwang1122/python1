"""
class Inheritance
class level function
class level attribute (field, variable)
"""
from enum import Enum

class Mood(Enum): # Mood class inherits from Enum class, inherits from other's class is big advantage.
    DUDE = 1 # class level attribute
    HAPPY = 3
    JAZZY = 5
    OOFY = 9

    def describe(self): # instance level function
        return self.name, self.value

    @classmethod
    def favorite_mood(cls): # class level function
        return cls.HAPPY


if __name__ == '__main__':
    try:
        x = Mood.favorite_mood() # call class level function by using the class name
        print(x)
        print(Mood.DUDE.value) # use class name to get class level attribute

        mood1 = Mood(1) # use value to get attribute
        print(type(mood1))
        print(mood1)
        print(mood1.favorite_mood())
    
        mood6 = Mood(6)
        print(mood6)

        mood6.describe()
    except Exception as error:
        print(error)

    print("End")
