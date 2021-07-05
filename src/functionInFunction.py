"""
Define function inside another function, protect inner function from calling outside unexpectedly.
1. protect inner function from 
2. 
"""

def parent():
    print("I'm parent.")
    def child1():
        print("I am an elder child...")
    def child2():
        print("I am a younger child...")

    child1()
    child2()
    return child2

if __name__ == '__main__': # build a test code block
    parent()
    # parent.child1()# python do not allow outside directly call inner functio
    x = parent()
    print(x)
    x()