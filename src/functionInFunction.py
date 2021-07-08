"""
Define function inside another function, 
1. protect inner function from calling outside unexpected.
2. return the child function to outside.
"""

def parent():
    print("I'm parent.")
    def child1():
        print("I am a elder child...")
    def child2():
        print("I am a younger child...")

    child1()
    child2()
    return child2

if __name__ == '__main__': # build a test code block
    parent()
    # parent.child1() # python don't allow outside directly call inner function.
    x = parent()
    print(x)
    x()