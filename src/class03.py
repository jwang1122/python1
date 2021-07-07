"""
Define a function inside the class
"""

class Robot:
    id = 1234
    def sayHello(self):
        print(f"Hello, I am robot {self.name}.") 

if __name__ == '__main__':
    obj = Robot()
    obj.name = "John"
    obj.sayHello()
    print(f"my ID is {obj.id}")