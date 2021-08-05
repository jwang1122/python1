class Stack:
    def __init__(self, name):
        self.name = name
        self.collection = []

    def __repr__(self):
        return self.name
    
    def push(self, obj):
        self.collection.append(obj)
    
    def pop(self):
        return self.collection.pop()

if __name__ == '__main__':
    s = Stack("roy")
    s.push(1)
    s.push(2)
    s.push("hello")
    s.push("world") # last in
    x = s.pop() # first out
    print(x)
    x = s.pop()
    print(x)
    s.push("roy")
    s.push("john")
    x = s.pop()
    print(x)
    x = s.pop()
    print(x)
    s.pop()
    s.pop()
    s.pop()