"""
access none public attributes: getter, setter and property
"""

class Robot:
    def __init__(self, inputName=None, energy=1000):
        self._name = inputName # create a new attribute called self.name
        self.__energy = energy

    def __repr__(self):
        return self._name + ": " + str(self.__energy)

    def sayHello(self): # every function defined inside class has first positional argument as itself.
        if self._name:
            print(f"Hello, I am robot {self._name}.") 
        else:
            print('Hi, I am a robot without name yet.')

    # Create setter, getter
    def getName(self): # getter
        return self._name
    
    def setName(self, newName): # setter
        # check authorization here
        self._name = newName

    def getEnergy(self):
        return self.__energy
    
    def setEnergy(self, newEnergy):
        self.__energy = newEnergy

    def delName(self):
        print("delName() is called!!")
        del self._name

    name = property(getName, setName, delName) # pass function as argument

if __name__ == '__main__': # test area for testing code above
    x = Robot("John Wang")
    x.sayHello()

    print(x.getName())
    print(x.getEnergy())
    x.setEnergy(2000) # recharge the battery
    print(x.getEnergy())

    print(x.name) # this will call getName() function
    x.name = "Amy" # this will call setName('Amy') function
    print(x.name)

    del x.name # this will call delName()
    # print(x) # make our program blows up.

    print("Done")