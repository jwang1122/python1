"""
Define a function inside the class
"""

class Robot:
    id = 1234
    def sayHello(self): # every method defined inside the class has first positional argument as itself
        print(f"Hello, I am robot {self.name}.")
    
    def add (self, x, y): # self does NOT count as an argument
        return x + y

if __name__ == '__main__':
    obj = Robot() # call default constructor to create instance of Robot.
    obj.name = "Kayden"
    obj.sayHello() # let robot object introduce itself, self argument does NOT count as 
    print(f"my ID is {obj.id}")

    x = obj.add(4, 5)
    print(x)

