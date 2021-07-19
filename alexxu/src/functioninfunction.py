"""
Define function inside another function, protect inner function from calling outside unexpected.

"""

def parent():
    print("I am kid")
    def child1():
        print("I am a elder child...")
    def child2():
        print('I am a younger child...')

        child1()
        child2()
        return child2

if __name__ == '__main__': #  build a test code block
    parent()
    # python do not allow outside directly call inner function. 
    x = parent()
    print(x)
    

