"""
access none public attributes: getter, setter, and property
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
    
    def getName(self): # getter
        # if checkUser():
        return self._name
    
    def setName(self, newName): # setter: ❓Why you use setter?
        #✔️I can do authorization check before change the _name
        self._name = newName

    def getEnergy(self):
        return self.__energy

    def setEnergy(self, newEnergy):
        self.__energy = newEnergy
    
    def delName(self):
        print("delName() is called!!!")
        del self._name

    name = property(getName, setName, delName)

if __name__ == '__main__':
    x = Robot("Kayden Gao")
    x.sayHello()

    print(x.getName())
    print(x.getEnergy())

    x.setName("Kayden") # 😄setter works!
    x.setEnergy(2000)
    print(x)

    print(x.name) # using getName()
    x.name = "Hongkai" # this operation will call our setter
    print(x)

    # del x.name # this will call delName() function
    # print(x)

    print("Done")