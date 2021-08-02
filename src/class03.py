"""
Define a function inside the class
"""

class Robot:
    id = 1234
    def sayHello(self): # every function defined inside class has first positional argument as itself.
        print(f"Hello, I am robot {self.name}.") 
    
    def add (self, x, y): # self does NOT count as a argument
        return x + y

if __name__ == '__main__':
    obj = Robot() # call default constructor to create instance of Robot.
    obj.name = "KaydentheDude"
    obj.sayHello() # let robot object introduce himself, self argument does NOT count as argument
    print(f"my ID is {obj.id}")

    x = obj.add(4, 5)
    print(x)
