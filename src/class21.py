"""
Composition vs. inheritance
Engine is part of car, car compose a engine
"""
class Car:
    def __init__(self, model, manufacture, makeYear):
        self.model = model
        self.manufacture = manufacture
        self.makeYear = makeYear
    
    def __repr__(self):
        return ': '.join((self.manufacture, self.model))
    
    class Engine:
        def __init__(self, size):
            self.size = size
        def __repr__(self):
            return "Engine size: " + self.size

if __name__ == '__main__':
    car = Car("Camry", "Toyota", 2019)
    print(car)